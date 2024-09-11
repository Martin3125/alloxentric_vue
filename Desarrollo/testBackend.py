from fastapi.testclient import TestClient
from data_base import app

client = TestClient(app)

# def test_system_connections():
#     response = client.get("/api/inicio/")
#     assert response.status_code == 200

# def test_login():
#     response = client.post("/api/login", json={"email": "email@example.com", "pwd": "password"})
#     assert response.status_code == 200
#     assert "access_token" in response.json()

# def test_register_user():
#     response = client.post("/api/register", json={"nombre": "Test User", "email": "test@test.com", "pwd": "password"})
#     assert response.status_code == 201
#     assert response.json()["message"] == "Usuario registrado exitosamente"

# def test_password_confirmation():
#     response = client.post("/api/register", json={"nombre": "Test User", "email": "test@test.com", "pwd": "password", "confirm_pwd": "mismatch"})
#     assert response.status_code == 400
#     assert response.json() == {"detail": "Passwords do not match"}

# def test_unique_email():
#     client.post("/api/register", json={"nombre": "Test User", "email": "test@test.com", "pwd": "password"})
#     response = client.post("/api/register", json={"nombre": "Another User", "email": "test@test.com", "pwd": "password"})
#     assert response.status_code == 400
#     assert response.json() == {"detail": "El correo ya está registrado"}

# def test_register_cobranza():
#     response = client.post("/api/acciones", json={"accion_cobranza": "Cobranza Test", "fecha_cobranza": "2024-09-01", "intervalo": 1, "valor": 100})
#     assert response.status_code == 201
#     assert response.json()["message"] == "Acciones registradas exitosamente"

# def test_verify_cobranza():
#     response = client.get("/api/acciones")
#     assert response.status_code == 200
#     assert len(response.json()) > 0

# def test_file_upload():
#     with open("testfile.txt", "wb") as f:
#         f.write(b"Sample content")
#     with open("testfile.txt", "rb") as f:
#         response = client.post("/api/upload", files={"file": ("testfile.txt", f)})
#     assert response.status_code == 200
#     assert response.json() == {"filename": "testfile.txt"}

# def test_download_file():
#     response = client.get("/api/cobranza/download/1")
#     assert response.status_code == 200
#     assert "attachment" in response.headers["Content-Disposition"]

# CP-001: Probar las conexiones del sistema (Puertos)
def test_health_check():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_system_connections():
    archivo_id = 1  # o algún ID válido
    response = client.get(f"/api/inicio/{archivo_id}")
    assert response.status_code == 200

# CP-002: Permitir autenticarse en el sistema
def test_login():
    response = client.post("/api/login", json={"email": "user@example.com", "pwd": "string"})
    assert response.status_code == 200
    assert response.json()["message"] == "Inicio de sesión exitoso"

# CP-003: Registrar a un nuevo usuario en la base de datos
def test_register_user():
    response = client.post("/api/register", json={"nombre": "Test User1", "email": "test1@example.com", "pwd": "password1", "confirm_password": "password1"})
    assert response.status_code == 200
    assert response.json()["message"] == "Usuario registrado exitosamente"

# CP-004: Verificar la confirmación de contraseña
def test_register_user_password_confirmation():
    response = client.post("/api/register", json={"nombre": "Test User", "email": "test@example.com", "pwd": "password", "confirm_password": "password"})
    assert response.status_code == 200
    assert response.json()["message"] == "Usuario registrado exitosamente"

# CP-005: Registrar un usuario y que no se repitan los correos
def test_register_user_duplicate_email():
    # Registrar un usuario
    response = client.post("/api/register", json={"nombre": "Duplicate User", "email": "duplicate@example.com", "pwd": "password", "confirm_password": "password"})
    assert response.status_code == 200
    assert response.json()["message"] == "Usuario registrado exitosamente"

    # Intentar registrar otro usuario con el mismo correo
    response = client.post("/api/register", json={"nombre": "Another User", "email": "duplicate@example.com", "pwd": "Another", "confirm_password": "Another"})
    assert response.status_code == 400
    assert response.json()["detail"] == "El correo ya está registrado"

# CP-006: Visualización de los últimos archivos subidos
def test_view_uploaded_files():
    archivo_id = 22
    response = client.get(f"/api/inicio/{archivo_id}")
    assert response.status_code == 200
    assert len(response.json()) > 0

# CP-007: Visualización de los procesamientos programados
def test_view_scheduled_processes():
    procesamiento_id = "66e10e2b5c227a0ec290128a"
    response = client.get(f"/api/procesamiento_P/{procesamiento_id}")
    assert response.status_code == 200
    assert len(response.json()) > 0

# CP-008: Poder cancelar los procesamientos programados
def test_cancel_scheduled_process():
    procesamiento_id = "66e10f706bdc71277ff4cfc7"
    response = client.delete(f"/api/procesamiento_P/{procesamiento_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Procesamiento eliminado exitosamente"

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