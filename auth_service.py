class Usuario:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.intentos_fallidos = 0
        self.bloqueado = False

class AuthService:
    def __init__(self):
        # Simulación de base de datos de usuarios
        self._usuarios = {
            "juan@ejemplo.com": Usuario("juan@ejemplo.com", "Clave123!"),
            "maria@ejemplo.com": Usuario("maria@ejemplo.com", "Segura456!")
        }
        self.MAX_INTENTOS = 3
    
    def login(self, email: str, password: str) -> dict:
        """
        Intenta autenticar a un usuario.
        Retorna un diccionario con el resultado de la operación.
        """
        if not email or not password:
            return {"exito": False, "mensaje": "Email y contraseña son requeridos"}
            
        if not self._es_email_valido(email):
            return {"exito": False, "mensaje": "Formato de email inválido"}
            
        usuario = self._usuarios.get(email)
        if not usuario:
            return {"exito": False, "mensaje": "Usuario no encontrado"}
            
        if usuario.bloqueado:
            return {"exito": False, "mensaje": "Usuario bloqueado por múltiples intentos fallidos"}
            
        if usuario.password != password:
            usuario.intentos_fallidos += 1
            if usuario.intentos_fallidos >= self.MAX_INTENTOS:
                usuario.bloqueado = True
                return {"exito": False, "mensaje": "Usuario bloqueado por múltiples intentos fallidos"}
            return {"exito": False, "mensaje": f"Contraseña incorrecta. Intentos restantes: {self.MAX_INTENTOS - usuario.intentos_fallidos}"}
            
        # Reset de intentos fallidos al lograr login exitoso
        usuario.intentos_fallidos = 0
        return {"exito": True, "mensaje": "Login exitoso"}
    
    def _es_email_valido(self, email: str) -> bool:
        """Validación básica de formato de email"""
        return '@' in email and '.' in email.split('@')[1]