from fastapi.testclient import TestClient
from data_base import app
import os
from datetime import datetime
from bson import ObjectId
import pytest
from fastapi import status
from pymongo.collection import Collection
from unittest.mock import MagicMock

client = TestClient(app)


# CP-001: Probar las conexiones del sistema (Puertos)
def test_health_check():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

# def test_system_connections():
#     archivo_id = 1  # o algún ID válido
#     response = client.get(f"/api/inicio/{archivo_id}")
#     assert response.status_code == 200

# # CP-002: Permitir autenticarse en el sistema
# def test_login():
#     response = client.post("/api/login", json={"email": "user@example.com", "pwd": "string"})
#     assert response.status_code == 200
#     assert response.json()["message"] == "Inicio de sesión exitoso"

# # CP-003: Registrar a un nuevo usuario en la base de datos
# def test_register_user():
#     response = client.post("/api/register", json={"nombre": "Test User1", "email": "test1@example.com", "pwd": "password1", "confirm_password": "password1"})
#     assert response.status_code == 200
#     assert response.json()["message"] == "Usuario registrado exitosamente"

# # CP-004: Verificar la confirmación de contraseña
# def test_register_user_password_confirmation():
#     response = client.post("/api/register", json={"nombre": "Test User", "email": "test@example.com", "pwd": "password", "confirm_password": "password"})
#     assert response.status_code == 200
#     assert response.json()["message"] == "Usuario registrado exitosamente"

# # CP-005: Registrar un usuario y que no se repitan los correos
# def test_register_user_duplicate_email():
#     # Registrar un usuario
#     response = client.post("/api/register", json={"nombre": "Duplicate User", "email": "duplicate@example.com", "pwd": "password", "confirm_password": "password"})
#     assert response.status_code == 200
#     assert response.json()["message"] == "Usuario registrado exitosamente"

#     # Intentar registrar otro usuario con el mismo correo
#     response = client.post("/api/register", json={"nombre": "Another User", "email": "duplicate@example.com", "pwd": "Another", "confirm_password": "Another"})
#     assert response.status_code == 400
#     assert response.json()["detail"] == "El correo ya está registrado"

# CP-006: Visualización de los últimos archivos subidos
# Test para la ruta "/api/inicio"
@pytest.fixture
def mock_archivos_collection(monkeypatch):
    # Mockea la colección `archivos_collection`
    mock_collection = MagicMock(spec=Collection)
    monkeypatch.setattr("data_base.archivos_collection", mock_collection)
    return mock_collection

def test_get_all_archivos_success(mock_archivos_collection):
    # Mockea el comportamiento de la colección para devolver archivos
    mock_archivos_collection.find.return_value = [
        {"_id": "6452bfc2f2e8f2a6f6e19b3a", "nombre": "archivo1.txt", "fecha": "2024-11-12"},
        {"_id": "6452bfc2f2e8f2a6f6e19b3b", "nombre": "archivo2.txt", "fecha": "2024-11-10"},
    ]

    response = client.get("/api/inicio")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
        {"Id_archivo": "6452bfc2f2e8f2a6f6e19b3a", "nombre": "archivo1.txt", "fecha": "2024-11-12"},
        {"Id_archivo": "6452bfc2f2e8f2a6f6e19b3b", "nombre": "archivo2.txt", "fecha": "2024-11-10"},
    ]

def test_get_all_archivos_not_found(mock_archivos_collection):
    # Mockea la colección para devolver una lista vacía
    mock_archivos_collection.find.return_value = []

    response = client.get("/api/inicio")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "No se encontraron archivos."}


# CP-009: Registrar una fecha y hora de procesamiento
def test_register_process():
    response = client.post("/api/procesamiento_P", json={"nombre": "Test Process", "fecha": "2024-09-05", "hora": "12:00:00"})
    assert response.status_code == 200
    assert response.json()["message"] == "Procesamiento registrado exitosamente"

# CP-010: Crear, modificar o actualizar la acción de cobranza
def test_register_or_update_action():
    response = client.post("/api/acciones", json=[{"accion_cobranza": "Test Action", "fecha_cobranza": "2024-09-05", "intervalo": 10, "valor": 100}])
    assert response.status_code == 200
    assert response.json()["message"] == "Acciones registradas exitosamente"

# CP-011: Visualizar todas las acciones de cobranza
def test_view_all_actions():
    response = client.get("/api/acciones")
    assert response.status_code == 200
    assert len(response.json()) > 0

# CP-012: Upload (Generar resultados)
def test_upload_file():
    # Ruta del archivo de prueba
    file_path = "uploads\Archivo de prueba.csv"

    # Asegurarse de que el archivo existe antes de ejecutar la prueba
    assert os.path.exists(file_path), f"El archivo {file_path} no existe."

    # Abrimos el archivo en modo binario para simular la carga de un archivo real
    with open(file_path, "rb") as file:
        # Enviamos el archivo al endpoint /api/upload
        response = client.post(
            "/api/upload",
            files={"file": ("Archivo de prueba.csv", file, "text/csv")}
        )

    # Comprobamos que la respuesta sea 200 OK
    assert response.status_code == 200

    # Verificamos el contenido de la respuesta
    json_response = response.json()
    assert json_response["status"] == "success"
    assert "id_procesamiento" in json_response
    assert "predicciones" in json_response

    # Opcional: comprobamos que las predicciones no estén vacías
    assert len(json_response["predicciones"]) > 0


 # CP-013:   # Prueba para obtener todos los archivos
def test_get_all_archivos():
    response = client.get("/api/inicio")
    if response.status_code == 404:
        assert response.json()["detail"] == "No se encontraron archivos."
    else:
        assert response.status_code == 200
        archivos = response.json()
        assert isinstance(archivos, list)  # Debe devolver una lista
        if archivos:
            assert "Id_archivo" in archivos[0]
            assert "nombre" in archivos[0]
            assert "fecha" in archivos[0]

# CP-014: # Prueba para obtener todos los procesamientos programados
def test_get_all_procesamientos():
    response = client.get("/api/procesamiento_P")
    if response.status_code == 404:
        assert response.json()["detail"] == "No se encontraron procesamientos."
    else:
        assert response.status_code == 200
        procesamientos = response.json()
        assert isinstance(procesamientos, list)
        if procesamientos:
            assert "Id_procesamiento" in procesamientos[0]
            assert "nombre" in procesamientos[0]
            assert "fecha" in procesamientos[0]
            assert "hora" in procesamientos[0]



# CP-016:# Prueba para crear un nuevo procesamiento
def test_register_procesamiento():
    procesamiento_data = {
        "nombre": "Procesamiento de prueba",
        "fecha": datetime.now().date().isoformat(),
        "hora": datetime.now().time().isoformat(),
    }
    response = client.post("/api/procesamiento_P", json=procesamiento_data)
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["success"] == True
    assert json_response["message"] == "Procesamiento registrado exitosamente"

# CP-017: # Prueba para registrar o actualizar acciones de cobranza
def test_register_or_update_accion():
    # Crear datos de ejemplo para registrar
    accion_data = [
        {
            "accion_cobranza": "Cobranza 1",
            "Id_accion": "123",
            "fecha_cobranza": datetime.now().date().isoformat(),
            "intervalo": 30,
            "valor": 100.0
        }
    ]

    response = client.post("/api/acciones", json=accion_data)
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["success"] == True
    assert json_response["message"] == "Acciones registradas exitosamente"
    
    # Probar actualización de una acción existente
    updated_data = [
        {
            "accion_cobranza": "Cobranza 1",
            "Id_accion": "123",
            "fecha_cobranza": datetime.now().date().isoformat(),
            "intervalo": 45,
            "valor": 150.0
        }
    ]
    
    response = client.post("/api/acciones", json=updated_data)
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["success"] == True
    assert json_response["message"] == "Acciones registradas exitosamente"

# CP-018# Prueba para obtener todas las acciones de cobranza
def test_get_acciones_cobranza():
    response = client.get("/api/acciones")
    if response.status_code == 404:
        assert response.json()["detail"] == "No se encontraron acciones de cobranza"
    else:
        assert response.status_code == 200
        acciones = response.json()
        assert isinstance(acciones, list)
        if acciones:
            assert "Id_accion" in acciones[0]
            assert "accion_cobranza" in acciones[0]
            assert "fecha_cobranza" in acciones[0]
            assert "intervalo" in acciones[0]
            assert "valor" in acciones[0]

# CP-019# Prueba para obtener todas las acciones de cobranza con otro endpoint
def test_obtener_acciones_cobranza():
    response = client.get("/acciones_cobranza")
    if response.status_code == 404:
        assert response.json()["detail"] == "No se encontraron acciones de cobranza"
    else:
        assert response.status_code == 200
        acciones = response.json()
        assert isinstance(acciones, list)
        if acciones:
            assert "Id_accion" in acciones[0]
            assert "accion_cobranza" in acciones[0]
            assert "fecha_cobranza" in acciones[0]
            assert "intervalo" in acciones[0]
            assert "valor" in acciones[0]

# CP-020# Prueba para obtener todos los resultados
def test_obtener_resultados():
    response = client.get("/resultados")
    if response.status_code == 404:
        assert response.json()["detail"] == "No se encontraron resultados"
    else:
        assert response.status_code == 200
        resultados = response.json()
        assert isinstance(resultados, list)
        if resultados:
            assert "id_procesamiento" in resultados[0]
            assert "documento_cargado" in resultados[0]
            assert "fecha_carga" in resultados[0]
            assert "registro_deudores" in resultados[0]
            assert "deudores_contactar" in resultados[0]
            assert "deudores" in resultados[0]
            assert "precio" in resultados[0]
            assert "accion_predicha" in resultados[0]


# CP-022# Prueba para obtener el reporte de métricas
def test_get_metrics():
    response = client.get("/api/metrics")
    if response.status_code == 404:
        assert response.json()["error"] == "metrics_report.json not found"
    else:
        assert response.status_code == 200
        metrics_data = response.json()
        assert isinstance(metrics_data, dict)  # Asegúrate de que sea un diccionario

# CP-023# Prueba para obtener el reporte de métricas de entrenamiento
def test_get_train_metrics_report():
    response = client.get("/api/train_metrics_report")
    if response.status_code == 404:
        assert response.json()["error"] == "train_metrics_report.json not found"
    else:
        assert response.status_code == 200
        metrics_data = response.json()
        assert isinstance(metrics_data, dict)  # Asegúrate de que sea un diccionario