from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, constr
from pymongo import MongoClient
from bson.objectid import ObjectId
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# # Configura los orígenes permitidos
# origins = [
#     "http://localhost:8080",  # Reemplaza con la URL del frontend si es diferente
#     "http://127.0.0.1:8080",
# ]

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


# Definición del modelo de usuario
class User(BaseModel):
    nombre: constr(max_length=16)
    email: EmailStr
    pwd: constr(min_length=6, max_length=12)

@app.post("/api/register")
async def register_user(user: User):
    if users_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="El correo ya está registrado")

    new_user = {
        "nombre": user.nombre,
        "email": user.email,
        "pwd": user.pwd,
        "tipo_usuario": False  # Asumiendo que es un usuario normal por defecto
    }

    users_collection.insert_one(new_user)
    return {"success": True, "message": "Usuario registrado exitosamente"}

