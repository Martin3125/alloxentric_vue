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

import requests

# URL base de la API
API_URL = "http://localhost:8000/api"  # Cambia según la configuración de tu API

# Función para probar si el endpoint GET para obtener acciones de cobranza responde correctamente
def test_get_acciones_cobranza():
    print("---- Probando /api/acciones (GET) ----")
    try:
        response = requests.get(f"{API_URL}/acciones")
        # Verificamos el código de respuesta y que el contenido devuelto sea el esperado
        assert response.status_code in [200, 404], "Fallo en conexión: Código de estado inesperado"
        if response.status_code == 200:
            acciones = response.json()
            assert isinstance(acciones, list), "La respuesta no es una lista de acciones"
            print("Prueba de conexión /api/acciones (GET): OK")
        else:
            print("No se encontraron acciones de cobranza, como se esperaba.")
    except Exception as e:
        print(f"Error en /api/acciones (GET): {e}")

# Función para probar si el endpoint POST es vulnerable a inyección SQL
def test_acciones_post_sql_injection():
    print("---- Probando Inyección SQL en /api/acciones (POST) ----")
    payloads = [
        "' OR '1'='1",
        "'; DROP TABLE AccionCobranza; --",
        "' UNION SELECT * FROM AccionCobranza; --"
    ]
    for payload in payloads:
        accion_payload = {
            "Id_accion": payload,  # Prueba de inyección en el campo Id_accion
            "accion_cobranza": "Cobranza Test",
            "fecha_cobranza": "2024-11-12",
            "intervalo": 10,
            "valor": 100.0
        }
        try:
            response = requests.post(f"{API_URL}/acciones", json=[accion_payload])
            assert response.status_code != 500, f"Inyección SQL detectada con payload {payload}"
            print(f"Inyección SQL en /api/acciones (POST) con payload '{payload}': Sin vulnerabilidad detectada")
        except Exception as e:
            print(f"Error en prueba de inyección SQL POST /api/acciones con payload '{payload}': {e}")

# Función para probar si el endpoint POST para registrar o actualizar acciones funciona correctamente
def test_register_update_accion():
    print("---- Probando registro y actualización de acción en /api/acciones (POST) ----")
    accion = {
        "Id_accion": "1234",  # Este Id es solo un ejemplo
        "accion_cobranza": "Cobranza Test",
        "fecha_cobranza": "2024-11-12",
        "intervalo": 10,
        "valor": 100.0
    }
    try:
        response = requests.post(f"{API_URL}/acciones", json=[accion])
        # Verificamos si la acción fue registrada o actualizada correctamente
        assert response.status_code == 200, f"Fallo en registro/actualización: {response.status_code}"
        assert response.json().get("success") is True, "La respuesta no indica éxito"
        print("Prueba de registro/actualización en /api/acciones (POST): OK")
    except Exception as e:
        print(f"Error en registro/actualización en /api/acciones (POST): {e}")

# Función para probar el endpoint GET alternativo para obtener todas las acciones de cobranza
def test_obtener_acciones_cobranza():
    print("---- Probando /acciones_cobranza (GET) ----")
    try:
        response = requests.get(f"{API_URL.replace('/api', '')}/acciones_cobranza")
        assert response.status_code in [200, 404], "Fallo en conexión: Código de estado inesperado"
        if response.status_code == 200:
            acciones = response.json()
            assert isinstance(acciones, list), "La respuesta no es una lista de acciones"
            print("Prueba de conexión /acciones_cobranza (GET): OK")
        else:
            print("No se encontraron acciones de cobranza en /acciones_cobranza, como se esperaba.")
    except Exception as e:
        print(f"Error en /acciones_cobranza (GET): {e}")

# Función para probar si el endpoint GET es vulnerable a inyección SQL
def test_get_acciones_sql_injection():
    print("---- Probando Inyección SQL en /acciones_cobranza (GET) ----")
    payloads = [
        "' OR '1'='1",
        "'; DROP TABLE AccionCobranza; --",
        "' UNION SELECT * FROM AccionCobranza; --"
    ]
    for payload in payloads:
        try:
            response = requests.get(f"{API_URL.replace('/api', '')}/acciones_cobranza?test_param={payload}")
            assert response.status_code != 500, f"Inyección SQL detectada con payload {payload}"
            print(f"Inyección SQL en /acciones_cobranza (GET) con payload '{payload}': Sin vulnerabilidad detectada")
        except Exception as e:
            print(f"Error en prueba de inyección SQL /acciones_cobranza (GET) con payload '{payload}': {e}")

# Función para probar si el endpoint de creación o actualización es vulnerable a un ataque DoS
def test_acciones_dos():
    print("---- Probando DoS en /api/acciones ----")
    try:
        responses = []
        accion = {
            "Id_accion": "1234",
            "accion_cobranza": "Cobranza Test",
            "fecha_cobranza": "2024-11-12",
            "intervalo": 10,
            "valor": 100.0
        }
        for _ in range(100):  # Realiza 100 peticiones para simular DoS
            response = requests.post(f"{API_URL}/acciones", json=[accion])
            responses.append(response)

        assert all(res.status_code == 200 for res in responses), "Fallo en prueba DoS: No todos los códigos son 200"
        print("Prueba de DoS en /api/acciones: OK")
    except Exception as e:
        print(f"Error en prueba DoS en /api/acciones: {e}")

# Ejecutar todas las pruebas
if __name__ == "__main__":
    test_get_acciones_cobranza()
    test_acciones_post_sql_injection()
    test_register_update_accion()
    test_obtener_acciones_cobranza()
    test_get_acciones_sql_injection()
    test_acciones_dos()
