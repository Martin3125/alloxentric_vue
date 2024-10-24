import requests
import time

# Configuración de la API
API_URL = "http://localhost:8000/api"  # Cambia esto según tu configuración

# Caso de Prueba 3: Control de Acceso a los Registros de Cobranza
def test_access_control():
    # Intentar acceder a registros como un usuario sin permisos
    response = requests.get(f"{API_URL}/cobranza/records", headers={"Authorization": "Bearer token_de_usuario_sin_permisos"})
    assert response.status_code == 403  # Debería ser 403 Forbidden
    print("Caso de Prueba 3: Control de Acceso OK")

# Caso de Prueba 4: Pruebas de Inyección SQL
def test_sql_injection():
    payloads = [
        "' OR '1'='1'; --",
        "'; DROP TABLE users; --",
        "' UNION SELECT * FROM users; --"
    ]
    
    for payload in payloads:
        response = requests.post(f"{API_URL}/login", json={
            "email": f"user@example.com{payload}",
            "pwd": "contraseña123"
        })
        assert response.status_code == 400  # Debería fallar
        print(f"Caso de Prueba 4: Inyección SQL con payload '{payload}' OK")

# Caso de Prueba 5: Gestión de Sesiones y Protección contra Secuestro de Sesión
def test_session_management():
    # Iniciar sesión
    login_response = requests.post(f"{API_URL}/login", json={
        "email": "usuario@example.com",
        "pwd": "contraseña123"
    })
    assert login_response.status_code == 200
    token = login_response.json().get("token")

    # Intentar acceder a la sesión de otro usuario manipulando la cookie (token)
    response = requests.get(f"{API_URL}/protected_endpoint", headers={"Authorization": "Bearer token_manipulado"})
    assert response.status_code == 403  # Debería ser 403 Forbidden

    # Simular inactividad
    time.sleep(31)  # Esperar más del tiempo de expiración de sesión
    response_after_timeout = requests.get(f"{API_URL}/protected_endpoint", headers={"Authorization": token})
    assert response_after_timeout.status_code == 401  # Debería ser 401 Unauthorized

    print("Caso de Prueba 5: Gestión de Sesiones OK")

# Caso de Prueba 6: Pruebas de Denegación de Servicio (DoS)
def test_dos_attack():
    # Enviar múltiples peticiones simultáneas
    responses = []
    for _ in range(100):  # Intentar 100 peticiones
        response = requests.get(f"{API_URL}/some_endpoint")  # Cambia por el endpoint a probar
        responses.append(response)

    # Comprobar que el sistema no ha fallado
    assert all(res.status_code == 200 for res in responses)  # Todos deberían ser 200 OK
    print("Caso de Prueba 6: Pruebas de Denegación de Servicio OK")

# Caso de Prueba 7: Registro y Monitoreo de Actividad
def test_logging_and_monitoring():
    # Intentar acceso no autorizado
    response = requests.get(f"{API_URL}/protected_endpoint", headers={"Authorization": "Bearer token_de_usuario_sin_permisos"})
    assert response.status_code == 403  # Debería ser 403 Forbidden

    # Comprobar en los logs (esto dependerá de cómo implementes el registro)
    log_response = requests.get(f"{API_URL}/logs")  # Endpoint para obtener logs
    logs = log_response.json()
    assert any("403 Forbidden" in log for log in logs)  # Debería haber un registro de acceso no autorizado

    print("Caso de Prueba 7: Registro y Monitoreo de Actividad OK")

# Ejecutar las pruebas
if __name__ == "__main__":
    test_access_control()
    test_sql_injection()
    test_session_management()
    test_dos_attack()
    test_logging_and_monitoring()
