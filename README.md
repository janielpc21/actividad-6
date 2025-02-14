# actividad-6

# Proyecto de Pruebas Unitarias - Autenticación y Ecommerce

Este proyecto demuestra la implementación de pruebas unitarias en Python utilizando pytest para dos sistemas: un servicio de autenticación y un sistema básico de ecommerce.

## Estructura del Proyecto

```
├── auth_service.py
├── test_auth_service.py
├── ecommerce.py
├── test_ecommerce.py
└── README.md
```

## Requisitos

- Python 3.x
- pytest

Para instalar las dependencias:
```bash
pip install pytest
```

## Servicio de Autenticación

### Características
- Gestión de usuarios con email y contraseña
- Sistema de bloqueo después de múltiples intentos fallidos
- Validación de credenciales
- Control de intentos de inicio de sesión

### Pruebas Implementadas
- Login exitoso
- Login con credenciales incorrectas
- Bloqueo de cuenta tras múltiples intentos
- Validación de formato de email
- Campos vacíos o inválidos

## Sistema de Ecommerce

### Características
- Gestión de productos con precio, stock y categoría
- Carrito de compras por usuario
- Cálculo de totales
- Validación de stock
- Operaciones CRUD en el carrito

### Pruebas Implementadas
- Agregar productos al catálogo
- Validar productos duplicados
- Agregar/remover productos del carrito
- Actualizar cantidades
- Validar límites de stock
- Calcular totales del carrito

## Ejecución de Pruebas

Para ejecutar todas las pruebas:
```bash
pytest
```

Para ejecutar pruebas específicas:
```bash
pytest test_auth_service.py    # Solo pruebas de autenticación
pytest test_ecommerce.py      # Solo pruebas de ecommerce
```

Para ver detalles de las pruebas:
```bash
pytest -v
```

## Estructura de las Pruebas

### Fixtures
Se utilizan fixtures de pytest para:
- Crear instancias limpias de los servicios
- Preparar datos de prueba
- Mantener el estado entre pruebas

### Patrón AAA
Las pruebas siguen el patrón Arrange-Act-Assert:
1. **Arrange**: Preparación de datos y condiciones
2. **Act**: Ejecución de la funcionalidad a probar
3. **Assert**: Verificación de resultados

## Buenas Prácticas Implementadas

1. Nombres descriptivos de pruebas
2. Una aserción principal por prueba
3. Uso de fixtures para código reutilizable
4. Pruebas independientes
5. Cobertura de casos positivos y negativos
6. Manejo de errores y casos límite

## Contribución

Para contribuir al proyecto:
1. Fork del repositorio
2. Crear una rama para tu característica
3. Commit de tus cambios
4. Push a la rama
5. Crear un Pull Request

## Licencia

MIT License - ver archivo LICENSE para más detalles
