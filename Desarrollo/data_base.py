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

# Definición del modelo de usuario
class User(BaseModel):
    nombre: constr(max_length=16)
    email: EmailStr
    pwd: constr(min_length=6, max_length=12)
    confirm_password: constr(min_length=6, max_length=12)   # Este campo es opcional

class LoginUser(BaseModel):
    email: EmailStr
    pwd: constr(min_length=6, max_length=12)



# class Sin_acciones(BaseModel):
#     nombre_cobranza: constr(max_length=16)
#     fecha_cobranza: datetime
#     intervalo: int
#     valor: float

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

class Resultados(BaseModel):
    ID: int
    nombre_documento: str
    fecha: date
    registro_gente: float
    accion: str
    gente_contactar: float

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


# #Endpoint de inicio
# @app.get("/api/inicio/{archivo_id}", response_model=List[Archivos])
# async def get_archivos(archivo_id: str):
#     archivos = list(archivos_collection.find({"Id_archivo": archivo_id}))

#     if not archivos:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontraron archivos.")
#     # Transformar _id de ObjectId a string para que sea compatible con el modelo
#     # for archivo in archivos:
#     #     archivo["Id_archivo"] = str(archivo["_id"])
#     #     del archivo["_id"]
#     archivo_modificados = []
#     for archivo in archivos:
#         archivo_modificado = {
#             "Id_archivo": archivo["Id_archivo"],
#             "nombre": archivo["nombre"],
#             "fecha": archivo["fecha"]  
#         }
#         archivo_modificados.append(archivo_modificado)    
#     # Devolver los documentos junto con un mensaje de éxito
#     return archivo_modificados

# #Endpoint de Procesamientos programados
# @app.get("/api/procesamiento_P/{procesamiento_id}", response_model=List[Procesamiento])
# async def get_Procesamientos(procesamiento_id: str):
#     procesamientos = list(procesamiento_collection.find({"Id_procesamiento": procesamiento_id}))

#     if not procesamientos:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontraron Procesamientos.")
    
#     procesamiento_modificados = []
#     for procesamiento in procesamientos:
#         procesamiento_modificado = {
#             "Id_procesamiento": procesamiento["Id_procesamiento"],
#             "nombre": procesamiento["nombre"],
#             "fecha": procesamiento["fecha"],
#             "hora": procesamiento["hora"]  
#         }
#         procesamiento_modificados.append(procesamiento_modificado)    
#     # Devolver los documentos junto con un mensaje de éxito
#     return procesamiento_modificados
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

# @app.get("/ejemplo/")
# async def ejemplo():
#     respuesta = dict(mensaje="Éxito", codigo=200)
#     return respuesta

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
