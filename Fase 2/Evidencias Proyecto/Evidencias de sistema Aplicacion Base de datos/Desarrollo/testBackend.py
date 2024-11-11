from fastapi.testclient import TestClient
from data_base import app
import os
from datetime import datetime
from bson import ObjectId

client = TestClient(app)

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

# # CP-015# Prueba para eliminar un procesamiento por ID
# def test_delete_procesamiento():
#     # Primero, crea un procesamiento para eliminarlo después
#     new_id = str(ObjectId())
#     procesamiento_data = {
#         "Id_procesamiento": new_id,
#         "nombre": "Procesamiento de prueba",
#         "fecha": datetime.now().date().isoformat(),
#         "hora": datetime.now().time().isoformat(),
#     }
#     client.post("/api/procesamiento_P", json=procesamiento_data)

#     # Intenta eliminar el procesamiento recién creado
#     response = client.delete(f"/api/procesamiento_P/{new_id}")
#     assert response.status_code == 200
#     assert response.json()["message"] == "Procesamiento eliminado exitosamente"

#     # Verifica que el procesamiento ya no exista
#     response = client.delete(f"/api/procesamiento_P/{new_id}")
#     assert response.status_code == 404
#     assert response.json()["detail"] == "Procesamiento no encontrado."

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

# CP-021# Prueba para crear un nuevo resultado
def test_crear_resultado():
    resultado_data = {
        "Id_resultados": "12345",
        "id_procesamiento": "proc123",
        "documento_cargado": "documento_test.csv",
        "fecha_carga": "2024-11-01",
        "registro_deudores": 10,
        "deudores_contactar": 5,
        "deudores": "deudor1, deudor2",
        "precio": 1500.0,
        "accion_predicha": "Cobranza"
    }
    
    response = client.post("/resultados", json=resultado_data)
    assert response.status_code == 201
    json_response = response.json()
    assert json_response["Id_resultados"] == "12345"
    assert json_response["id_procesamiento"] == "proc123"
    assert json_response["documento_cargado"] == "documento_test.csv"
    assert json_response["fecha_carga"] == "2024-11-01"
    assert json_response["registro_deudores"] == 10
    assert json_response["deudores_contactar"] == 5
    assert json_response["deudores"] == "deudor1, deudor2"
    assert json_response["precio"] == 1500.0
    assert json_response["accion_predicha"] == "Cobranza"

    # Intentar crear un resultado con el mismo ID (debería fallar)
    response = client.post("/resultados", json=resultado_data)
    assert response.status_code == 400
    assert response.json()["detail"] == "El resultado ya existe."

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