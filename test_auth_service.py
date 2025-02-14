import pytest
from auth_service import AuthService

@pytest.fixture
def auth_service():
    """Fixture que proporciona una instancia limpia de AuthService para cada prueba"""
    return AuthService()

def test_login_exitoso(auth_service):
    # Arrange
    email = "juan@ejemplo.com"
    password = "Clave123!"
    
    # Act
    resultado = auth_service.login(email, password)
    
    # Assert
    assert resultado["exito"] == True
    assert resultado["mensaje"] == "Login exitoso"

def test_login_password_incorrecta(auth_service):
    # Arrange
    email = "juan@ejemplo.com"
    password = "ClaveIncorrecta"
    
    # Act
    resultado = auth_service.login(email, password)
    
    # Assert
    assert resultado["exito"] == False
    assert "Contraseña incorrecta" in resultado["mensaje"]

def test_login_usuario_no_existe(auth_service):
    # Arrange
    email = "noexiste@ejemplo.com"
    password = "Cualquier"
    
    # Act
    resultado = auth_service.login(email, password)
    
    # Assert
    assert resultado["exito"] == False
    assert resultado["mensaje"] == "Usuario no encontrado"

def test_bloqueo_tras_intentos_fallidos(auth_service):
    # Arrange
    email = "juan@ejemplo.com"
    password_incorrecta = "ClaveIncorrecta"
    
    # Act
    # Intentamos 3 veces con contraseña incorrecta
    for _ in range(3):
        resultado = auth_service.login(email, password_incorrecta)
    
    # Assert
    assert resultado["exito"] == False
    assert "bloqueado" in resultado["mensaje"]
    
    # Verificamos que incluso con la contraseña correcta no pueda acceder
    resultado_final = auth_service.login(email, "Clave123!")
    assert resultado_final["exito"] == False
    assert "bloqueado" in resultado_final["mensaje"]

def test_email_invalido(auth_service):
    # Arrange
    email = "correo_invalido"
    password = "Cualquier"
    
    # Act
    resultado = auth_service.login(email, password)
    
    # Assert
    assert resultado["exito"] == False
    assert resultado["mensaje"] == "Formato de email inválido"

def test_campos_vacios(auth_service):
    # Test con email vacío
    resultado1 = auth_service.login("", "password")
    assert resultado1["exito"] == False
    assert "requeridos" in resultado1["mensaje"]
    
    # Test con password vacía
    resultado2 = auth_service.login("juan@ejemplo.com", "")
    assert resultado2["exito"] == False
    assert "requeridos" in resultado2["mensaje"]