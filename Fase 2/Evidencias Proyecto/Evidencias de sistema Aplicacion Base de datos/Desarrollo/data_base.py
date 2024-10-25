from fastapi import FastAPI, HTTPException, status
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
reporte_collection = db["Reporte"]
archivos_collection = db["Archivos"]
procesamiento_collection = db["Procesamiento"]
directorios_collection = db["directorios"]
resultados_collection  = db["Resultados"]
predicciones_collection = db["predicciones"]

# Definición del modelo de usuario
class User(BaseModel):
    nombre: constr(max_length=16)
    email: EmailStr
    pwd: constr(min_length=6, max_length=12)
    confirm_password: constr(min_length=6, max_length=12)   # Este campo es opcional

class LoginUser(BaseModel):
    email: EmailStr
    pwd: constr(min_length=6, max_length=12)

# Model for individual actions
class AccionCobranza(BaseModel):
    Id_accion: Optional[str]  # Optional because it will be generated by MongoDB
    accion_cobranza: str
    fecha_cobranza: str
    intervalo: int
    valor: float


class Deudor(BaseModel):
    ID_deudor: int
    nombre_deudor: str
    numtelefono: str
    email: EmailStr
    Deuda: float

class Archivos(BaseModel):
    Id_archivo: Optional[str] 
    nombre: str
    fecha: date

class Procesamiento(BaseModel):
    Id_procesamiento: Optional[str] 
    nombre: str
    fecha: date
    hora: time

# Modelo para las predicciones
class Prediccion(BaseModel):
    accion_predicha: str
    total_deudores: int

class Resultados(BaseModel):
    Id_resultados: int
    nombre: str
    fecha: str
    registro: int
    tipo: str
    cantidad: str
    precio: float
    predicciones: List[Prediccion]

class Reporte(BaseModel):
    ID_deudor: Optional[str]
    nombre_deudor: str 
    accion: str  
    fecha_envio: date
    intervalo: str 
    fecha_estimada: date
    demora: str  
    fecha_real: date
    debe_pagar: float
    valor_pagar: float

class KMeansModel(BaseModel):
    model_name: str  
    model_file: str
    created_at: datetime

class Pago(BaseModel):
    id_pago: int  
    user: str
    nombreEs: str  
    h_inicio: str  
    fecha_Pago: str 
    totalPago: str 
    
# Modelo Pydantic para crear un directorio
class Directorio(BaseModel):
    nombre_directorio: str

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
            "Id_archivo": archivo["Id_archivo"],
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

    # Hacer predicciones
    try:
        df_group = predict(df_final)  # Ahora se pasa df_final a la función predict
        predicciones_resultados = df_group.to_dict(orient="records")

          # Preparar documentos para MongoDB
        predicciones_documentos = [
            {
                "accion_predicha": pred["accion_predicha"],
                "total_deudores": pred["total_deudores"]
            }
            for pred in predicciones_resultados
        ]

        # Guardar en MongoDB
        predicciones_collection.insert_many(predicciones_documentos)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al predecir: {str(e)}")

    return JSONResponse(content={
        'status': 'success',
        'predicciones': df_group.to_dict(orient="records")
    })

predicciones_resultados = [] 
#--------------------------------Predicción directa---------------------------------------------------------------

@app.post('/api/predict')
async def predict_endpoint(request: Request):
    global predicciones_resultados  # Declarar la variable global
    try:
        data = await request.json()
        if not data:
            return JSONResponse(content={"error": "No se recibieron datos."}, status_code=400)

        features = pd.DataFrame(data)

        # Manejar valores NaN
        if features.isnull().values.any():
            features = features.dropna()

        df_group = predict(features)  # Cambié aquí: ahora solo se pasa un argumento
        predicciones_resultados = df_group.to_dict(orient="records")

          # Preparar documentos para MongoDB
        predicciones_documentos = [
            {
                "accion_predicha": pred["accion_predicha"],
                "total_deudores": pred["total_deudores"]
            }
            for pred in predicciones_resultados
        ]

        # Guardar en MongoDB
        predicciones_collection.insert_many(predicciones_documentos)

        return JSONResponse(content=predicciones_resultados)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en la solicitud de predicción: {str(e)}")

# Endpoint GET para obtener los resultados de predicción
@app.get('/api/resultados')
async def get_resultados():
    return JSONResponse(content={
        'status': 'success',
        'predicciones': predicciones_resultados  # Devolver los resultados almacenados
    })

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
@app.get("/resultados", response_model=List[Resultados])
def obtener_resultados():
    resultados = list(resultados_collection.find())  # Obtener todos los resultados
    if not resultados:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontraron resultados.")
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

#----------------------------------predicciones-------------------------------------------------------

@app.get('/api/predicciones')
async def get_predicciones():
    try:
        # Buscar solo el campo 'predicciones' en la base de datos
        predicciones = list(predicciones_collection.find({}, {"predicciones": 1, "_id": 0}))
        
        # Si no se encuentran predicciones
        if not predicciones:
            raise HTTPException(status_code=404, detail="No se encontraron predicciones.")
        
        # Aplanar las predicciones si es necesario
        predicciones_lista = [pred for doc in predicciones for pred in doc['predicciones']]

        return JSONResponse(content={
            'status': 'success',
            'predicciones': predicciones_lista
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener predicciones: {str(e)}")