from fastapi import FastAPI, HTTPException, status, Form
from pydantic import BaseModel, EmailStr, constr
from pymongo import MongoClient
from bson.objectid import ObjectId
from fastapi.middleware.cors import CORSMiddleware
from passlib.context import CryptContext
from typing import List
from pydantic import BaseModel, Field
from datetime import datetime
from pydantic import BaseModel, Field, validator
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date, time, datetime
from fastapi.security import OAuth2PasswordBearer
from fastapi import Query
from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import joblib
import pandas as pd
from werkzeug.utils import secure_filename
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import os
from fastapi import FastAPI, Request


from fastapi import FastAPI, Request, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import os
from data_preparation import prepare_data
from modeling import run_kmeans, run_lstm

from models import User, LoginUser, AccionCobranza, Deudor, Archivos, Procesamiento, Prediccion, Resultados, Reporte, Modelo, KMeansModel, Pago, Directorio

import uuid

import random
import string

# app = FastAPI()

# Inicializar la aplicación FastAPI
app = FastAPI()
import os

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],
)

# Conexión a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["alloxentric"]
users_collection = db["usuarios"]
# accioncobranza_collection = db["AccionCobranza"]
cobranza_collection = db["Cobranza"]
Sin_acciones_collection = db["Sin_acciones"] 
acciones_collection = db["AccionCobranza"]
reporte_collection = db["Reporte_desempeño"]
archivos_collection = db["Archivos"]
procesamiento_collection = db["Procesamiento"]
directorios_collection = db["directorios"]
resultados_collection  = db["Resultados"]
predicciones_collection = db["predicciones"]
modelo_collection = db["modelo"]



#Endpoint de prueba de conexiones 
@app.get("/api/health")
def health_check():
    return {"status": "ok"}

#Endpoint de registro
@app.post("/api/register")
async def register_user(user: User):
    if users_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="El correo ya está registrado")
    
    if user.confirm_password and user.pwd != user.confirm_password:
        raise HTTPException(status_code=400, detail="Las contraseñas no coinciden")
    
    # Hash de la contraseña
    hashed_pwd = pwd_context.hash(user.pwd)
    new_user = {
        "nombre": user.nombre,
        "email": user.email,
        "pwd": hashed_pwd,
        "tipo_usuario": False  # Asumiendo que es un usuario normal por defecto
    }

    users_collection.insert_one(new_user)
    return {"success": True, "message": "Usuario registrado exitosamente"}

#Endpoint de login
@app.post("/api/login")
async def login_user(user: LoginUser):
    # Verificar si el usuario existe
    user_record = users_collection.find_one({"email": user.email})
    if not user_record:
        raise HTTPException(status_code=400, detail="Correo o contraseña incorrectos")

    # Verificar la contraseña
    if not pwd_context.verify(user.pwd, user_record["pwd"]):
        raise HTTPException(status_code=400, detail="Correo o contraseña incorrectos")
    
    return {"success": True, "message": "Inicio de sesión exitoso"}

# Endpoint para obtener todos los archivos
@app.get("/api/inicio", response_model=List[Archivos])
async def get_all_archivos():
    archivos = list(archivos_collection.find())

    if not archivos:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontraron archivos.")
    
    archivo_modificados = []
    for archivo in archivos:
        archivo_modificado = {
            "Id_archivo": str(archivo["_id"]),  # Convierte ObjectId a str
            "nombre": archivo["nombre"],
            "fecha": archivo["fecha"]
        }
        archivo_modificados.append(archivo_modificado)
        
    return archivo_modificados

# Endpoint para obtener todos los procesamientos programados
@app.get("/api/procesamiento_P", response_model=List[Procesamiento])
async def get_all_procesamientos():
    procesamientos = list(procesamiento_collection.find())

    if not procesamientos:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontraron procesamientos.")
    
    procesamiento_modificados = []
    for procesamiento in procesamientos:
        procesamiento_modificado = {
            "Id_procesamiento": procesamiento["Id_procesamiento"],
            "nombre": procesamiento["nombre"],
            "fecha": procesamiento["fecha"],
            "hora": procesamiento["hora"]
        }
        procesamiento_modificados.append(procesamiento_modificado)
        
    return procesamiento_modificados

# Nuevo Endpoint para eliminar un procesamiento por ID
@app.delete("/api/procesamiento_P/{procesamiento_id}")
async def delete_Procesamiento(procesamiento_id: str):
    result = procesamiento_collection.delete_one({"Id_procesamiento": procesamiento_id})

    if result.deleted_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Procesamiento no encontrado.")
    
    return {"message": "Procesamiento eliminado exitosamente"}

#Endpoint de crear un procesamiento
@app.post("/api/procesamiento_P")
async def register_procesamiento(procesamiento: Procesamiento):
    try:
        # Generar un nuevo ObjectId y usarlo para Id_procesamiento
        new_id = str(ObjectId())

        # Verificar si el procesamiento ya está registrado (por Id_procesamiento)
        if procesamiento_collection.find_one({"Id_procesamiento": new_id}):
            raise HTTPException(status_code=400, detail="El procesamiento ya está registrado")
        # # Verificar si el procesamiento ya está registrado
        # if procesamiento_collection.find_one({"Id_procesamiento": procesamiento.Id_procesamiento}):
        #     raise HTTPException(status_code=400, detail="El procesamiento ya está registrado")

        # Convertir la hora en segundos desde el inicio del día
        time_field_seconds = procesamiento.hora.hour * 3600 + procesamiento.hora.minute * 60 + procesamiento.hora.second

        # Crear el nuevo documento para la base de datos
        new_proces = {
            "Id_procesamiento" : new_id,
            "nombre": procesamiento.nombre,
            "fecha": procesamiento.fecha.isoformat(),  # Convertir la fecha a cadena en formato ISO
            "hora": procesamiento.hora.isoformat(),    # Convertir la hora a cadena en formato ISO
            "time_field": time_field_seconds  # Hora en segundos
        }

        # Insertar el documento en la base de datos
        procesamiento_collection.insert_one(new_proces)

        return {"success": True, "message": "Procesamiento registrado exitosamente"}
    except Exception as e:
            # Manejo de excepciones y depuración
            print(f"Error al registrar el procesamiento: {e}")
            raise HTTPException(status_code=500, detail="Error interno del servidor")


#Endpoint de cobranza
@app.post("/api/acciones")
async def register_or_update_accion(acciones: List[AccionCobranza]):
    for accion in acciones:
        # Check if action with the same `accion_cobranza` and `Id_accion` exists
        existing_accion = acciones_collection.find_one({
            "accion_cobranza": accion.accion_cobranza,
            "Id_accion": accion.Id_accion
        })
        
        if existing_accion:
            # Update existing record
            result = acciones_collection.update_one(
                {"_id": existing_accion["_id"]},
                {"$set": {
                    "fecha_cobranza": accion.fecha_cobranza,
                    "intervalo": accion.intervalo,
                    "valor": accion.valor
                }}
            )
            if result.modified_count == 0:
                raise HTTPException(status_code=400, detail="No se pudo actualizar el registro")
        else:
            # Insert new record
            new_accion = accion.dict()
            del new_accion["Id_accion"]  # Remove Id_accion as it should not be in the document
            acciones_collection.insert_one(new_accion)
    
    return {"success": True, "message": "Acciones registradas exitosamente"}

@app.get("/api/acciones")
def get_acciones():
    return [{"accion": "test"}]

# base de los demas endpoints 
# Simulación de base de datos en memoria
documentos_db = {}
procesamientos_db = {}
resultados_db = {}

# Procesamiento - POST: Iniciar procesamiento de documentos subidos
@app.post("/api/procesamiento", response_model=str)
def iniciar_procesamiento(documentos_ids: List[str]):
    if not documentos_ids:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="IDs de documentos faltantes.")
    
    # Verificar si todos los documentos existen
    for doc_id in documentos_ids:
        if doc_id not in documentos_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Documentos no encontrados.")
    
    # Simulación de procesamiento
    proceso_id = "proc_" + "_".join(documentos_ids)
    procesamientos_db[proceso_id] = {"documentos": documentos_ids}
    
    return f"ID del proceso iniciado: {proceso_id}"

# Procesamiento (Resultados) - GET: Resultados del procesamiento ejecutado
@app.get("/procesamiento/{proceso_id}", response_model=dict)
def obtener_resultados_procesamiento(proceso_id: str):
    if proceso_id not in procesamientos_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Procesamiento no encontrado.")
    
    try:
        resultados = procesamientos_db[proceso_id]
        return resultados
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error - Error del servidor.")

# Cargar resultados del período anterior en los Directorios - GET
@app.get("/resultados/periodo-anterior/directorios/{resultado_id}", response_model=str)
def cargar_resultados_directorios(resultado_id: str):
    if resultado_id not in resultados_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resultados no encontrados.")
    
    # Simulación de carga de resultados en directorios
    return f"Carga de los resultados realizados en el periodo anterior según el directorio: {resultado_id}"

# Cargar resultados del período anterior para los Archivos - GET
@app.get("/resultados/periodo-anterior/archivos/{resultado_id}", response_model=str)
def cargar_resultados_archivos(resultado_id: str):
    if resultado_id not in resultados_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resultados no encontrados.")
    
    # Simulación de carga de resultados en archivos
    return f"Carga de los resultados realizados en el periodo anterior según el archivo: {resultado_id}"

# Generar resultados del período - GET
@app.get("/resultados/generar/{resultado_id}", response_model=List[dict])
def generar_resultados(resultado_id: str):
    if resultado_id not in resultados_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resultados no encontrados.")
    
    try:
        # Simulación de generación de resultados
        resultados = [{"id": resultado_id, "resultado": "Datos del procesamiento generado"}]
        return resultados
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error - Error del servidor.")

# Informes (Reportes de la última carga) - GET
@app.get("/informes/ultima-carga/{reporte_id}", response_model=str)
def visualizar_reporte_ultima_carga(reporte_id: str):
    if reporte_id not in resultados_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resultados no encontrados.")
    
    # Simulación de visualización de reportes de la última carga
    return f"Visualización de los reportes de la última carga: {reporte_id}"

# Informes (Reportes de desempeño) - GET
# @app.get("/informes/desempeno/{deudor_id}", response_model=str)
# def visualizar_reporte_desempeno(deudor_id: str):
#     if deudor_id not in resultados_db:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Deudor no encontrado.")
    
#     # Simulación de visualización de reporte de desempeño
#     return f"Visualización del desempeño del deudor con ID: {deudor_id}"
@app.get("/api/reportes/{deudor_id}", response_model=List[Reporte])
async def get_reporte_deudor(deudor_id: str):
    # Buscar todos los reportes para el deudor específico
    reportes = list(reporte_collection.find({"ID_deudor": deudor_id}))
    
    if not reportes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Reportes no encontrados para el deudor especificado.")

    # Convertir ObjectId a string y ajustar los datos para la respuesta
    reportes_modificados = []
    for reporte in reportes:
        reporte_modificado = {
            "ID_deudor": reporte["ID_deudor"],
            "nombre_deudor": reporte["nombre_deudor"],
            "accion": reporte["accion"],
            "fecha_envio": reporte["fecha_envio"],
            "intervalo": reporte["intervalo"],
            "fecha_estimada": reporte["fecha_estimada"],
            "demora": reporte["demora"],
            "fecha_real": reporte["fecha_real"],
            "debe_pagar": reporte["debe_pagar"],
            "valor_pagar": reporte["valor_pagar"]
        }
        reportes_modificados.append(reporte_modificado)
    
    return reportes_modificados

@app.get("/api/deudores_ids", response_model=List[str])
async def get_all_deudores_ids():
    # Obtener todos los IDs de los deudores de la base de datos
    deudores = list(reporte_collection.find({}, {"ID_deudor": 1, "_id": 0}))  # Solo obtener los IDs
    deudor_ids = [deudor["ID_deudor"] for deudor in deudores]
    
    if not deudor_ids:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontraron deudores.")
    
    return deudor_ids


@app.post("/api/manipular-modelo")
async def update_weights(weights: List[float] = Form(...), n_samples: int = Form(...)):
    if len(weights) != 7:
        raise HTTPException(status_code=400, detail="Se requieren exactamente 7 pesos.")

    # Crear un diccionario con los nombres de los campos
    modelo_data_dict = {
        "pond_sin_acciones": weights[0],
        "pond_correo_electronico": weights[1],
        "pond_sms": weights[2],
        "pond_whatsapp": weights[3],
        "pond_llamada_por_bot": weights[4],
        "pond_llamada_directa": weights[5],
        "pond_acciones_judiciales": weights[6],
        "n_samples": n_samples  # Añadir n_samples al diccionario
    }

    # Crear el modelo a partir del diccionario
    modelo_data = Modelo(**modelo_data_dict)

    # Buscar un documento existente
    existing_modelo = modelo_collection.find_one({})

    if existing_modelo:
        # Actualizar el documento existente
        result = modelo_collection.update_one(
            {"_id": existing_modelo["_id"]},
            {"$set": modelo_data.dict()}
        )
        if result.modified_count == 0:
            raise HTTPException(status_code=400, detail="No se pudo actualizar el registro")
    else:
        # Insertar un nuevo documento
        modelo_collection.insert_one(modelo_data.dict())

    return JSONResponse(content={'message': 'Pesos actualizados correctamente'}, status_code=200)


@app.get("/api/modelo")
async def get_modelo():
    existing_modelo = modelo_collection.find_one({})
    if existing_modelo:
        return JSONResponse(content=existing_modelo, status_code=200)
    else:
        raise HTTPException(status_code=404, detail="No se encontró ningún registro")
    


#--------------------------------Models---------------------------------------------------------------


# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = 'uploads/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Procesar archivo CSV
def process_file(file_path):
    try:
        # Leer el archivo CSV
        data = pd.read_csv(file_path, sep=';')

        if data.empty:
            raise ValueError("El archivo CSV está vacío.")

        # Preparar datos usando la función definida en data_preparation.py
        df_final = prepare_data(data)

        return df_final
    except KeyError as e:
        raise HTTPException(status_code=400, detail=f"Error de columna: {str(e)}")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Error de datos: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar el archivo: {str(e)}")

# Predicciones
def predict(df_final):
    try:
        # Aplicar K-Means
        df_final = run_kmeans(df_final)

        # Ahora se puede llamar a run_lstm directamente con df_final
        df_deudores_grouped = run_lstm(df_final)  # Aquí se llama a run_lstm

        return df_deudores_grouped  # Devolvemos el DataFrame agrupado directamente
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al predecir: {str(e)}")

# Subida de archivo
@app.post('/api/upload')
async def upload_file(file: UploadFile = File(...)):
    if not file:
        raise HTTPException(status_code=400, detail="No se envió ningún archivo")

    # Guardar archivo temporalmente
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Procesar el archivo
    try:
        df_final = process_file(file_path)  # Procesar el archivo para obtener df_final
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar el archivo: {str(e)}")

    # Generar un ID único de procesamiento
    id_procesamiento = f"{random.choice(string.ascii_uppercase)}{random.randint(1, 999):03d}"

    # Hacer predicciones
    try:
        df_group = predict(df_final)  # Obtener predicciones
        predicciones_resultados = df_group.to_dict(orient="records")

        # Guardar el archivo y la fecha en MongoDB
        archivo_documento = {
            "nombre": file.filename,
            "fecha": datetime.now().strftime("%Y-%m-%d")
        }
        archivos_collection.insert_one(archivo_documento) 

        # Calcular la suma de total_deudores para registro_deudores
        registro_deudores_total = sum(pred["total_deudores"] for pred in predicciones_resultados)

        # Preparar documentos para MongoDB (colección de resultados)
        resultados_documentos = [
            {
                "id_procesamiento": id_procesamiento,  # ID de procesamiento único para todas las predicciones
                "documento_cargado": file.filename,
                "fecha_carga": datetime.now().strftime("%Y-%m-%d"),
                "accion_predicha": pred["accion_predicha"],  # Acción de cobranza
                "total_deudores": pred["total_deudores"],  # Total de deudores para la acción predicha
                "registro_deudores": registro_deudores_total,  # Total de predicciones generadas
                "deudores_contactar": pred["total_deudores"],  # Total de deudores para cada acción
                "precio": 0.0  # Ajustar lógica del precio si es necesario
            }
            for pred in predicciones_resultados
        ]

        # Guardar en la colección de resultados de MongoDB
        resultados_collection.insert_many(resultados_documentos)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al predecir: {str(e)}")

    return JSONResponse(content={
        'status': 'success',
        'id_procesamiento': id_procesamiento,  # ID único del procesamiento
        'predicciones': predicciones_resultados
    })

predicciones_resultados = [] 



# Endpoint GET para obtener los resultados de predicción
# @app.get('/api/resultados')
# async def get_resultados():
#     return JSONResponse(content={
#         'status': 'success',
#         'predicciones': predicciones_resultados  # Devolver los resultados almacenados
#     })

# # Endpoint GET para obtener los resultados de predicción
# @app.get('/api/resultados')
# async def get_resultados():
#     # Recuperar las predicciones desde MongoDB
#     predicciones = list(predicciones_collection.find({}, {"_id": 0}))  # Excluir el campo _id para simplicidad
#     if not predicciones:
#         raise HTTPException(status_code=404, detail="No se encontraron predicciones.")

#     return JSONResponse(content={
#         'status': 'success',
#         'predicciones': predicciones
#     })

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000, log_level="info")




#--------------------------------directorios---------------------------------------------------------------


from fastapi import FastAPI, HTTPException, status
from pymongo import MongoClient
from pydantic import BaseModel
from typing import List


# Obtener todos los directorios - GET
@app.get("/directorios", response_model=List[str])
def obtener_directorios():
    directorios = directorios_collection.distinct("nombre_directorio")  # Obtener directorios únicos
    if not directorios:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontraron directorios.")
    return directorios

# Obtener archivos de un directorio - GET
@app.get("/directorios/{directorio}/archivos", response_model=List[str])
def obtener_archivos_de_directorio(directorio: str):
    directorio_obj = directorios_collection.find_one({"nombre_directorio": directorio})
    if not directorio_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Directorio no encontrado.")
    
    archivos = directorio_obj.get("archivos", [])  # Obtener los archivos del directorio
    return archivos
# Ver el contenido de un archivo - GET
@app.get("/directorios/{directorio}/archivos/{archivo}")
def ver_contenido_archivo(directorio: str, archivo: str):
    directorio_obj = directorios_collection.find_one({"nombre_directorio": directorio})
    if not directorio_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Directorio no encontrado.")
    
    archivos = directorio_obj.get("archivos", [])
    if archivo not in archivos:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Archivo no encontrado.")
    
    # Aquí puedes modificar para obtener el archivo desde el sistema de archivos si es necesario
    # En este ejemplo, se devuelve un texto simulado como contenido del archivo.
    contenido_archivo = f"Contenido del archivo {archivo} en el directorio {directorio}."
    
    return {"contenido": contenido_archivo}

# Crear un nuevo directorio - POST
@app.post("/directorios", status_code=status.HTTP_201_CREATED)
def crear_directorio(directorio: Directorio):
    # Verificar si ya existe el directorio
    if directorios_collection.find_one({"nombre_directorio": directorio.nombre_directorio}):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El directorio ya existe.")
    
    # Crear un nuevo directorio
    nuevo_directorio = {
        "nombre_directorio": directorio.nombre_directorio,
        "archivos": []  # Lista vacía de archivos por defecto
    }
    
    # Insertar el nuevo directorio en la colección
    directorios_collection.insert_one(nuevo_directorio)
    
    return {"mensaje": "Directorio creado exitosamente", "directorio": directorio.nombre_directorio}

# Eliminar un directorio - DELETE
@app.delete("/directorios/{directorio}", status_code=status.HTTP_200_OK)
def eliminar_directorio(directorio: str):
    resultado = directorios_collection.delete_one({"nombre_directorio": directorio})
    
    if resultado.deleted_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Directorio no encontrado.")
    
    return {"mensaje": "Directorio eliminado exitosamente"}


# Ruta donde se guardarán los archivos localmente
BASE_DIR = "directorios"  # Cambia esta ruta a donde quieras almacenar los archivos

# Subir un archivo a un directorio específico - POST
@app.post("/directorios/{directorio}/subir_archivo")
async def subir_archivo(directorio: str, file: UploadFile = File(...)):
    # Verificar si el directorio existe en MongoDB
    directorio_obj = directorios_collection.find_one({"nombre_directorio": directorio})
    if not directorio_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Directorio no encontrado.")

    # Crear la ruta completa del archivo
    directorio_path = os.path.join(BASE_DIR, directorio)
    if not os.path.exists(directorio_path):
        os.makedirs(directorio_path)  # Crear el directorio si no existe

    file_path = os.path.join(directorio_path, file.filename)

    # Guardar el archivo en el sistema de archivos
    with open(file_path, "wb") as f:
        f.write(await file.read())

    # Agregar el archivo a la lista de archivos del directorio en MongoDB
    directorios_collection.update_one(
        {"nombre_directorio": directorio},
        {"$addToSet": {"archivos": file.filename}}  # $addToSet asegura que no haya duplicados
    )

    return {"mensaje": f"Archivo {file.filename} subido correctamente al directorio {directorio}."}


#--------------------------------Resultados---------------------------------------------------------------
# main.py
from fastapi import FastAPI, HTTPException, status
from pymongo import MongoClient
from typing import List

# Obtener todos los resultados - GET
# @app.get("/resultados", response_model=List[Resultados])
# async def obtener_resultados():
#     resultados = []
#     for resultado in resultados_collection.find():
#         resultado["id_procesamiento"] = resultado["id_procesamiento"]
#         resultado["documento_cargado"] = resultado["documento_cargado"]
#         resultado["fecha_carga"] = resultado["fecha_carga"]
#         resultado["registro_deudores"] = resultado["registro_deudores"]
#         # # resultado["acciones_cobranza"] = resultado["acciones_cobranza"]
#         # # resultado["deudores_contactar"] = resultado["deudores_contactar"]
#         # resultado.setdefault("predicciones", [])
#         resultado["precio"] = resultado["precio"]
        
#         # predicciones = list(predicciones_collection.find({"id_procesamiento": resultado["id_procesamiento"]}))
#         # resultado["predicciones"] = [Prediccion(**prediccion) for prediccion in predicciones]
#         resultados.append(Resultados(**resultado))  # Usa el modelo para la respuesta
#     return resultados

@app.get("/resultados", response_model=List[Resultados])
async def obtener_resultados():
    resultados = []
    
    # Iterar sobre los documentos en la colección `resultados`
    for resultado in resultados_collection.find():
        # Asegurarse de que todos los campos estén presentes en el diccionario
        resultado_dict = {
            "id_procesamiento": resultado.get("id_procesamiento", ""),
            "documento_cargado": resultado.get("documento_cargado", ""),
            "fecha_carga": resultado.get("fecha_carga", ""),  # Obtener la fecha del documento
            "registro_deudores": resultado.get("registro_deudores", 0),
            "deudores_contactar": resultado.get("deudores_contactar", 0),
            "precio": resultado.get("precio", 0.0),
            "accion_predicha": resultado.get("accion_predicha", "")
        }

        # Crear una instancia de Resultados y agregarla a la lista
        resultados.append(Resultados(**resultado_dict))
    
    # Retornar la lista de resultados
    return resultados



# Crear un nuevo resultado - POST
@app.post("/resultados", response_model=Resultados, status_code=status.HTTP_201_CREATED)
def crear_resultado(resultado: Resultados):
    # Verificar si ya existe un resultado con el mismo ID
    if resultados_collection.find_one({"Id_resultados": resultado.Id_resultados}):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El resultado ya existe.")
    
    # Insertar el nuevo resultado en la colección
    resultados_collection.insert_one(resultado.dict())
    
    return resultado


# Eliminar un resultado - DELETE
@app.delete("/resultados/{id_resultado}", status_code=status.HTTP_200_OK)
def eliminar_resultado(id_resultado: int):
    resultado = resultados_collection.delete_one({"Id_resultados": id_resultado})
    
    if resultado.deleted_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resultado no encontrado.")
    
    return {"mensaje": "Resultado eliminado exitosamente"}







# from fastapi import FastAPI, HTTPException, Depends
# from fastapi.security import OAuth2PasswordBearer
# from keycloak import KeycloakOpenID
#------------------------------Prueba keycloak--------------------------------------------------------------------

# # Configura Keycloak
# keycloak = KeycloakOpenID(
#     server_url='http://localhost:8080/auth/',
#     client_id='vue-app',
#     realm_name='Alloxentric',  # Reemplaza con el nombre de tu realm
# )

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

# @app.post("/api/login")
# async def login_user(token: str = Depends(oauth2_scheme)):
#     try:
#         # Verificar el token
#         user_info = keycloak.decode_token(token, options={"verify_signature": True})
#         email = user_info['preferred_username']

#         # Aquí puedes buscar al usuario en tu base de datos si es necesario
#         user_record = users_collection.find_one({"email": email})
#         if not user_record:
#             raise HTTPException(status_code=400, detail="Usuario no encontrado")

#         return {"success": True, "message": "Inicio de sesión exitoso", "user": user_record}

#     except Exception as e:
#         raise HTTPException(status_code=401, detail="Token inválido o expirado")

#----------------------------------------------------------------------------------------------------------------

#----------------------------------Keycloak-------------------------------------------------------

# from fastapi import Depends, HTTPException, Security
# from fastapi.security import OAuth2PasswordBearer
# from jose import JWTError, jwt

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# async def get_current_user(token: str = Depends(oauth2_scheme)):
#     try:
#         payload = jwt.decode(token, "YOUR_KEYCLOAK_PUBLIC_KEY", algorithms=["RS256"])
#         username: str = payload.get("preferred_username")
#         if username is None:
#             raise HTTPException(status_code=401, detail="Token no válido")
#         return username
#     except JWTError:
#         raise HTTPException(status_code=401, detail="Token no válido o expirado")

# @app.get("/api/protected-endpoint")
# async def protected_endpoint(username: str = Depends(get_current_user)):
#     return {"message": f"Hola, {username}"}
# from fastapi import FastAPI, Depends
# from keycloak import KeycloakOpenID



# @app.get("/api/protected-route")
# def protected_route(token: str = Depends(oauth2_scheme)):
#     try:
#         userinfo = keycloak.userinfo(token)
#         return {"message": "You are authenticated", "userinfo": userinfo}
#     except Exception as e:
#         return {"error": str(e)}





#----------------------------------------------KEYCLOAK FINAL---------------------------------------------------------
# from fastapi import FastAPI, Depends, HTTPException
# from fastapi.security import OAuth2PasswordBearer
# from keycloak import KeycloakOpenID


# keycloak_openid = KeycloakOpenID(server_url='http://localhost:8080/auth/',
#                                   client_id='vue-app',
#                                   realm_name='Alloxentric',
#                                   client_secret_key='LnI3hrpnmA9xWMspe4RfFAsleAzLQgrS')  # Solo si es un cliente confidencial

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# def verify_token(token: str = Depends(oauth2_scheme)):
#     try:
#         user_info = keycloak_openid.introspect(token)
#         if not user_info.get('active'):
#             raise HTTPException(status_code=401, detail="Invalid token")
#         return user_info
#     except Exception as e:
#         raise HTTPException(status_code=401, detail=str(e))

# @app.get("/api/protected")
# async def protected_route(user_info: dict = Depends(verify_token)):
#     return {"message": "This is a protected route", "user": user_info}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)
    
#---------------------------------------------------------------------------------------------------------------------------------------