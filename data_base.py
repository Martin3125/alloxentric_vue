from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, constr
from pymongo import MongoClient
from bson.objectid import ObjectId
from fastapi.middleware.cors import CORSMiddleware
from passlib.context import CryptContext
from typing import List

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


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
cobranza_collection = db["cobranza"] 

# Definición del modelo de usuario
class User(BaseModel):
    nombre: constr(max_length=16)
    email: EmailStr
    pwd: constr(min_length=6, max_length=12)

class LoginUser(BaseModel):
    email: EmailStr
    pwd: constr(min_length=6, max_length=12)

class Cobranza(BaseModel):
    ID: str
    accion_cobranza: str
    fecha_cobranza: str
    intervalo: int
    valor: float


@app.post("/api/register")
async def register_user(user: User):
    if users_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="El correo ya está registrado")
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

@app.post("/api/cobranza")
async def create_or_update_cobranza(cobranzas: List[Cobranza]):
    for cobranza in cobranzas:
        if cobranza.ID:
            # Actualizar el registro existente por id
            cobranza_collection.update_one(
                {"_id": ObjectId(cobranza.ID)},
                {"$set": {
                    "accion_cobranza": cobranza.accion_cobranza,
                    "fecha_cobranza": cobranza.fecha_cobranza,
                    "intervalo": cobranza.intervalo,
                    "valor": cobranza.valor
                }},
                upsert=True
            )
        else:
            # Insertar un nuevo registro si no tiene id
            new_cobranza = {
                "accion_cobranza": cobranza.accion_cobranza,
                "fecha_cobranza": cobranza.fecha_cobranza,
                "intervalo": cobranza.intervalo,
                "valor": cobranza.valor
            }
            cobranza_collection.insert_one(new_cobranza)
    return {"success": True, "message": "Cobranzas actualizadas exitosamente"}


@app.get("/api/cobranza/{ID}")
async def get_cobranza(ID: int):
    cobranza = cobranza_collection.find_one({"_id": ObjectId(ID)})
    if not cobranza:
        raise HTTPException(status_code=404, detail="Cobranza no encontrada")
    return {"cobranza": cobranza}

@app.get("/api/cobranza")
async def list_cobranza():
    cobranza_list = list(cobranza_collection.find())
    return {"cobranza": cobranza_list}