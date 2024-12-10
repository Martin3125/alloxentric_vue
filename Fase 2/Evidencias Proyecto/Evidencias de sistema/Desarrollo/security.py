# import requests

# # URL base de la API
# API_URL = "http://localhost:8000/api"  # Cambia según la configuración de tu API

# # Función para verificar si el endpoint responde correctamente
# def test_health_check():
#     print("---- Probando /api/health ----")
#     try:
#         response = requests.get(f"{API_URL}/health")
#         # Verificamos el código de respuesta y que el contenido devuelto sea el esperado
#         assert response.status_code == 200, "Fallo en conexión: Código de estado inesperado"
#         assert response.json().get("status") == "ok", "Respuesta incorrecta: estado de salud no es 'ok'"
#         print("Prueba de conexión /api/health: OK")
#     except Exception as e:
#         print(f"Error en /api/health: {e}")

# # Función para probar si el endpoint es vulnerable a inyección SQL
# def test_health_sql_injection():
#     print("---- Probando Inyección SQL en /api/health ----")
#     payloads = [
#         "' OR '1'='1",
#         "'; DROP TABLE users; --",
#         "' UNION SELECT * FROM users; --"
#     ]
#     for payload in payloads:
#         try:
#             # Realizamos una petición con payload de inyección SQL en un parámetro
#             response = requests.get(f"{API_URL}/health?test_param={payload}")
#             assert response.status_code != 500, f"Inyección SQL detectada con payload {payload}"
#             print(f"Inyección SQL en /api/health con payload '{payload}': Sin vulnerabilidad detectada")
#         except Exception as e:
#             print(f"Error en prueba de inyección SQL /api/health con payload '{payload}': {e}")

# # Función para probar si el endpoint es vulnerable a un ataque DoS
# def test_health_dos():
#     print("---- Probando DoS en /api/health ----")
#     try:
#         responses = []
#         for _ in range(100):  # Realiza 100 peticiones para simular DoS
#             response = requests.get(f"{API_URL}/health")
#             responses.append(response)

#         assert all(res.status_code == 200 for res in responses), "Fallo en prueba DoS: No todos los códigos son 200"
#         print("Prueba de DoS en /api/health: OK")
#     except Exception as e:
#         print(f"Error en prueba DoS en /api/health: {e}")

# # Función para probar si el endpoint está configurado correctamente para control de acceso
# def test_health_access_control():
#     print("---- Probando control de acceso en /api/health ----")
#     try:
#         # Intentamos acceder al endpoint sin un token de autorización
#         response = requests.get(f"{API_URL}/health")
#         assert response.status_code == 200, "El endpoint debería ser accesible sin autenticación si es un chequeo de salud"
#         print("Prueba de control de acceso /api/health: OK")
#     except Exception as e:
#         print(f"Error en control de acceso /api/health: {e}")




# # Función para probar si el endpoint `/api/inicio` responde correctamente y devuelve una lista de archivos
# def test_get_all_archivos():
#     print("---- Probando /api/inicio ----")
#     try:
#         response = requests.get(f"{API_URL}/inicio")
#         # Verificamos el código de respuesta y que el contenido devuelto sea el esperado
#         assert response.status_code in [200, 404], "Fallo en conexión: Código de estado inesperado"
#         if response.status_code == 200:
#             archivos = response.json()
#             assert isinstance(archivos, list), "La respuesta no es una lista de archivos"
#             print("Prueba de conexión /api/inicio: OK")
#         else:
#             print("No se encontraron archivos en /api/inicio, como se esperaba.")
#     except Exception as e:
#         print(f"Error en /api/inicio: {e}")

# # Función para probar si el endpoint `/api/inicio` es vulnerable a inyección SQL
# def test_inicio_sql_injection():
#     print("---- Probando Inyección SQL en /api/inicio ----")
#     payloads = [
#         "' OR '1'='1",
#         "'; DROP TABLE archivos; --",
#         "' UNION SELECT * FROM archivos; --"
#     ]
#     for payload in payloads:
#         try:
#             # Realizamos una petición con payload de inyección SQL en un parámetro
#             response = requests.get(f"{API_URL}/inicio?test_param={payload}")
#             assert response.status_code != 500, f"Inyección SQL detectada con payload {payload}"
#             print(f"Inyección SQL en /api/inicio con payload '{payload}': Sin vulnerabilidad detectada")
#         except Exception as e:
#             print(f"Error en prueba de inyección SQL /api/inicio con payload '{payload}': {e}")

# # Función para probar si el endpoint `/api/inicio` es vulnerable a un ataque DoS
# def test_inicio_dos():
#     print("---- Probando DoS en /api/inicio ----")
#     try:
#         responses = []
#         for _ in range(100):  # Realiza 100 peticiones para simular DoS
#             response = requests.get(f"{API_URL}/inicio")
#             responses.append(response)

#         assert all(res.status_code in [200, 404] for res in responses), "Fallo en prueba DoS: No todos los códigos son 200 o 404"
#         print("Prueba de DoS en /api/inicio: OK")
#     except Exception as e:
#         print(f"Error en prueba DoS en /api/inicio: {e}")

# # Función para probar si el endpoint `/api/inicio` está configurado correctamente para control de acceso
# def test_inicio_access_control():
#     print("---- Probando control de acceso en /api/inicio ----")
#     try:
#         # Intentamos acceder al endpoint sin un token de autorización
#         response = requests.get(f"{API_URL}/inicio")
#         assert response.status_code in [200, 404], "El endpoint debería ser accesible sin autenticación"
#         print("Prueba de control de acceso /api/inicio: OK")
#     except Exception as e:
#         print(f"Error en control de acceso /api/inicio: {e}")

# # Ejecutar todas las pruebas
# if __name__ == "__main__":
#     test_health_check()
#     test_get_all_archivos()
#     test_health_sql_injection()
#     test_inicio_sql_injection()
#     test_health_dos()
#     test_inicio_dos()
#     test_health_access_control()
#     test_inicio_access_control()

# import requests

# # URL base de la API
# API_URL = "http://localhost:8000/api"  # Cambia según la configuración de tu API

# # Función para verificar si el endpoint responde correctamente para obtener todos los procesamientos
# def test_get_all_procesamientos():
#     print("---- Probando /api/procesamiento_P ----")
#     try:
#         response = requests.get(f"{API_URL}/procesamiento_P")
#         # Verificamos el código de respuesta y que el contenido devuelto sea el esperado
#         assert response.status_code in [200, 404], "Fallo en conexión: Código de estado inesperado"
#         if response.status_code == 200:
#             procesamientos = response.json()
#             assert isinstance(procesamientos, list), "La respuesta no es una lista de procesamientos"
#             print("Prueba de conexión /api/procesamiento_P: OK")
#         else:
#             print("No se encontraron procesamientos en /api/procesamiento_P, como se esperaba.")
#     except Exception as e:
#         print(f"Error en /api/procesamiento_P: {e}")

# # Función para probar si el endpoint `/api/procesamiento_P` es vulnerable a inyección SQL
# def test_procesamiento_sql_injection():
#     print("---- Probando Inyección SQL en /api/procesamiento_P ----")
#     payloads = [
#         "' OR '1'='1",
#         "'; DROP TABLE procesamiento; --",
#         "' UNION SELECT * FROM procesamiento; --"
#     ]
#     for payload in payloads:
#         try:
#             # Realizamos una petición con payload de inyección SQL en un parámetro
#             response = requests.get(f"{API_URL}/procesamiento_P?test_param={payload}")
#             assert response.status_code != 500, f"Inyección SQL detectada con payload {payload}"
#             print(f"Inyección SQL en /api/procesamiento_P con payload '{payload}': Sin vulnerabilidad detectada")
#         except Exception as e:
#             print(f"Error en prueba de inyección SQL /api/procesamiento_P con payload '{payload}': {e}")

# # Función para probar si el endpoint `/api/procesamiento_P` es vulnerable a un ataque DoS
# def test_procesamiento_dos():
#     print("---- Probando DoS en /api/procesamiento_P ----")
#     try:
#         responses = []
#         for _ in range(100):  # Realiza 100 peticiones para simular DoS
#             response = requests.get(f"{API_URL}/procesamiento_P")
#             responses.append(response)

#         assert all(res.status_code in [200, 404] for res in responses), "Fallo en prueba DoS: No todos los códigos son 200 o 404"
#         print("Prueba de DoS en /api/procesamiento_P: OK")
#     except Exception as e:
#         print(f"Error en prueba DoS en /api/procesamiento_P: {e}")

# # Función para probar si el endpoint `/api/procesamiento_P` está configurado correctamente para control de acceso
# def test_procesamiento_access_control():
#     print("---- Probando control de acceso en /api/procesamiento_P ----")
#     try:
#         # Intentamos acceder al endpoint sin un token de autorización
#         response = requests.get(f"{API_URL}/procesamiento_P")
#         assert response.status_code in [200, 404], "El endpoint debería ser accesible sin autenticación"
#         print("Prueba de control de acceso /api/procesamiento_P: OK")
#     except Exception as e:
#         print(f"Error en control de acceso /api/procesamiento_P: {e}")

# # Función para probar el endpoint de creación de un procesamiento
# def test_create_procesamiento():
#     print("---- Probando creación de un procesamiento en /api/procesamiento_P (POST) ----")
#     new_procesamiento = {
#         "Id_procesamiento": "1234",  # Este Id es solo un ejemplo
#         "nombre": "Test Procesamiento",
#         "fecha": "2024-11-12",
#         "hora": "12:30:00"
#     }
#     try:
#         response = requests.post(f"{API_URL}/procesamiento_P", json=new_procesamiento)
#         # Verificamos si el procesamiento fue registrado correctamente
#         assert response.status_code == 200, f"Fallo al crear el procesamiento: {response.status_code}"
#         assert response.json().get("success") is True, "La respuesta no indica éxito"
#         print("Prueba de creación de procesamiento en /api/procesamiento_P: OK")
#     except Exception as e:
#         print(f"Error en creación de procesamiento en /api/procesamiento_P: {e}")

# # Función para probar si el endpoint de creación de un procesamiento es vulnerable a inyección
# def test_procesamiento_post_sql_injection():
#     print("---- Probando Inyección SQL en POST /api/procesamiento_P ----")
#     payloads = [
#         "' OR '1'='1",
#         "'; DROP TABLE procesamiento; --",
#         "' UNION SELECT * FROM procesamiento; --"
#     ]
#     for payload in payloads:
#         new_procesamiento = {
#             "Id_procesamiento": payload,  # Inyección en el campo Id_procesamiento
#             "nombre": "Test Inyección",
#             "fecha": "2024-11-12",
#             "hora": "12:30:00"
#         }
#         try:
#             response = requests.post(f"{API_URL}/procesamiento_P", json=new_procesamiento)
#             assert response.status_code != 500, f"Inyección SQL detectada con payload {payload}"
#             print(f"Inyección SQL en POST /api/procesamiento_P con payload '{payload}': Sin vulnerabilidad detectada")
#         except Exception as e:
#             print(f"Error en prueba de inyección SQL POST /api/procesamiento_P con payload '{payload}': {e}")

# # Ejecutar todas las pruebas
# if __name__ == "__main__":
#     test_get_all_procesamientos()
#     test_procesamiento_sql_injection()
#     test_procesamiento_dos()
#     test_procesamiento_access_control()
#     test_create_procesamiento()
#     test_procesamiento_post_sql_injection()


#ENDPOINT ACCIONES

# import requests
# import time

# # URL base de la API
# API_URL = "http://localhost:8000/api"  # Cambia según la configuración de tu API

# # Función para probar el endpoint GET para obtener acciones de cobranza
# def test_get_acciones_cobranza():
#     print("---- Probando /api/acciones (GET) ----")
#     try:
#         response = requests.get(f"{API_URL}/acciones")
#         assert response.status_code in [200, 404], "Fallo en conexión: Código de estado inesperado"
#         if response.status_code == 200:
#             acciones = response.json()
#             assert isinstance(acciones, list), "La respuesta no es una lista de acciones"
#             print("Prueba de conexión /api/acciones (GET): OK")
#         else:
#             print("No se encontraron acciones de cobranza, como se esperaba.")
#     except Exception as e:
#         print(f"Error en /api/acciones (GET): {e}")

# # Prueba de inyección NoSQL en el endpoint POST para verificar la resistencia a inyecciones
# def test_acciones_post_nosql_injection():
#     print("---- Probando Inyección NoSQL en /api/acciones (POST) ----")
#     payloads = [
#         {"$gt": ""},  # Prueba de NoSQL Injection con operador de comparación
#         {"$ne": None},  # Prueba de NoSQL Injection con operador de desigualdad
#         {"$or": [{"Id_accion": {"$gt": ""}}, {"accion_cobranza": "Cobranza Test"}]}
#     ]
#     for payload in payloads:
#         accion_payload = {
#             "Id_accion": payload,  # Inyección en campo Id_accion
#             "accion_cobranza": "Cobranza Test",
#             "fecha_cobranza": "2024-11-12",
#             "intervalo": 10,
#             "valor": 100.0
#         }
#         try:
#             response = requests.post(f"{API_URL}/acciones", json=[accion_payload])
#             assert response.status_code != 500, f"Inyección NoSQL detectada con payload {payload}"
#             print(f"Inyección NoSQL en /api/acciones (POST) con payload '{payload}': Sin vulnerabilidad detectada")
#         except Exception as e:
#             print(f"Error en prueba de inyección NoSQL POST /api/acciones con payload '{payload}': {e}")

# # Prueba de registro o actualización de una acción en el endpoint POST
# def test_register_update_accion():
#     print("---- Probando registro y actualización de acción en /api/acciones (POST) ----")
#     accion = {
#         "Id_accion": "1234",  # Este Id es solo un ejemplo
#         "accion_cobranza": "Cobranza Test",
#         "fecha_cobranza": "2024-11-12",
#         "intervalo": 10,
#         "valor": 100.0
#     }
#     try:
#         response = requests.post(f"{API_URL}/acciones", json=[accion])
#         assert response.status_code == 200, f"Fallo en registro/actualización: {response.status_code}"
#         assert response.json().get("success") is True, "La respuesta no indica éxito"
#         print("Prueba de registro/actualización en /api/acciones (POST): OK")
#     except Exception as e:
#         print(f"Error en registro/actualización en /api/acciones (POST): {e}")

# # Prueba para verificar que el endpoint GET no es vulnerable a NoSQL Injection
# def test_get_acciones_nosql_injection():
#     print("---- Probando Inyección NoSQL en /api/acciones (GET) ----")
#     payloads = [
#         {"$gt": ""},  # Prueba de inyección NoSQL
#         {"$ne": None},  # Prueba de inyección NoSQL
#         {"$or": [{"Id_accion": {"$gt": ""}}, {"accion_cobranza": "Cobranza Test"}]}
#     ]
#     for payload in payloads:
#         try:
#             response = requests.get(f"{API_URL}/acciones", params={"Id_accion": payload})
#             assert response.status_code != 500, f"Inyección NoSQL detectada con payload {payload}"
#             print(f"Inyección NoSQL en /api/acciones (GET) con payload '{payload}': Sin vulnerabilidad detectada")
#         except Exception as e:
#             print(f"Error en prueba de inyección NoSQL en /api/acciones (GET) con payload '{payload}': {e}")

# # Prueba de ataque DoS al endpoint POST de acciones
# def test_acciones_dos():
#     print("---- Probando DoS en /api/acciones ----")
#     try:
#         responses = []
#         accion = {
#             "Id_accion": "1234",
#             "accion_cobranza": "Cobranza Test",
#             "fecha_cobranza": "2024-11-12",
#             "intervalo": 10,
#             "valor": 100.0
#         }
#         for _ in range(50):  # Realiza 50 peticiones para simular un DoS leve
#             response = requests.post(f"{API_URL}/acciones", json=[accion])
#             responses.append(response)
#             time.sleep(0.1)  # Introducir una ligera pausa para no saturar completamente el servidor

#         assert all(res.status_code == 200 for res in responses), "Fallo en prueba DoS: No todos los códigos son 200"
#         print("Prueba de DoS en /api/acciones: OK")
#     except Exception as e:
#         print(f"Error en prueba DoS en /api/acciones: {e}")

# # Ejecutar todas las pruebas
# if __name__ == "__main__":
#     test_get_acciones_cobranza()
#     test_acciones_post_nosql_injection()
#     test_register_update_accion()
#     test_get_acciones_nosql_injection()
#     test_acciones_dos()


#ENDPOINT PROCESAMIENTO
import os
import requests
from datetime import datetime
from requests_toolbelt.multipart.encoder import MultipartEncoder

# URL base de la API
API_URL = "http://localhost:8000/api"  # Cambia según la configuración de tu API

# Ruta al archivo para pruebas
TEST_FILE_PATH = "uploads\Data_202409.csv"

# Función para probar la subida de archivos sin vulnerabilidades
def test_upload_file():
    print("---- Probando /api/upload (POST) ----")
    try:
        with open(TEST_FILE_PATH, "rb") as f:
            file_data = {"file": (os.path.basename(TEST_FILE_PATH), f, "text/csv")}
            encoder = MultipartEncoder(fields=file_data)
            headers = {"Content-Type": encoder.content_type}
            response = requests.post(f"{API_URL}/upload", data=encoder, headers=headers)
        
        # Verificación de respuesta exitosa
        assert response.status_code == 200, f"Error en subida de archivo: {response.status_code}"
        print("Prueba de carga de archivo: OK")
        
    except Exception as e:
        print(f"Error en /api/upload: {e}")

# Función para probar carga con archivo inválido
def test_invalid_file_type():
    print("---- Probando subida de archivo inválido en /api/upload ----")
    try:
        invalid_data = "archivo no compatible".encode()
        response = requests.post(f"{API_URL}/upload", files={"file": ("test.txt", invalid_data, "text/plain")})
        assert response.status_code == 400, "Se esperaba un error 400 para archivo no compatible"
        print("Prueba de archivo inválido: OK")
    except Exception as e:
        print(f"Error en prueba de archivo inválido: {e}")

# Función para probar la carga de archivo grande para detección de posibles vulnerabilidades DoS
def test_large_file_upload():
    print("---- Probando carga de archivo grande en /api/upload ----")
    try:
        large_file = "X" * 10**7  # 10 MB de datos
        response = requests.post(f"{API_URL}/upload", files={"file": ("large_test.csv", large_file, "text/csv")})
        assert response.status_code in [200, 413], "Esperaba un éxito o error 413 por tamaño excesivo"
        print("Prueba de archivo grande: OK")
    except Exception as e:
        print(f"Error en prueba de archivo grande: {e}")

# Función para probar si el endpoint POST es vulnerable a inyección de comandos
def test_command_injection_upload():
    print("---- Probando inyección de comandos en /api/upload ----")
    try:
        # Payload de inyección de comando
        command_injection_payload = "test; rm -rf /"
        response = requests.post(f"{API_URL}/upload", files={"file": ("command_inject.csv", command_injection_payload, "text/csv")})
        assert response.status_code != 500, "Posible vulnerabilidad de inyección detectada"
        print("Prueba de inyección de comandos: OK")
    except Exception as e:
        print(f"Error en prueba de inyección de comandos: {e}")

# Función para probar la concurrencia masiva para detectar posibles problemas de rendimiento
def test_massive_file_upload():
    print("---- Probando subida masiva de archivos (DoS) en /api/upload ----")
    try:
        responses = []
        for _ in range(50):  # Realiza 50 peticiones concurrentes
            with open(TEST_FILE_PATH, "rb") as f:
                file_data = {"file": (os.path.basename(TEST_FILE_PATH), f, "text/csv")}
                encoder = MultipartEncoder(fields=file_data)
                headers = {"Content-Type": encoder.content_type}
                response = requests.post(f"{API_URL}/upload", data=encoder, headers=headers)
                responses.append(response)
        
        assert all(res.status_code == 200 for res in responses), "Algunas peticiones fallaron en la prueba de DoS"
        print("Prueba masiva de DoS: OK")
    except Exception as e:
        print(f"Error en prueba de DoS masiva: {e}")

# Función para probar el límite en el número de predicciones
def test_prediction_count():
    print("---- Probando límite de predicciones en /api/upload ----")
    try:
        with open(TEST_FILE_PATH, "rb") as f:
            file_data = {"file": (os.path.basename(TEST_FILE_PATH), f, "text/csv")}
            encoder = MultipartEncoder(fields=file_data)
            headers = {"Content-Type": encoder.content_type}
            response = requests.post(f"{API_URL}/upload", data=encoder, headers=headers)
            result = response.json()
            # Verificar que no exceda un límite (ej. 100) de predicciones
            assert len(result.get("predicciones", [])) <= 100, "Número de predicciones excede el límite esperado"
            print("Prueba de límite de predicciones: OK")
    except Exception as e:
        print(f"Error en prueba de límite de predicciones: {e}")

# Ejecutar todas las pruebas
if __name__ == "__main__":
    test_upload_file()
    test_invalid_file_type()
    test_large_file_upload()
    test_command_injection_upload()
    test_massive_file_upload()
    test_prediction_count()
