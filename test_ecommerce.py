# test_ecommerce.py
import pytest
from decimal import Decimal
from ecommerce import TiendaEcommerce, Producto, Carrito

@pytest.fixture
def tienda():
    return TiendaEcommerce()

@pytest.fixture
def productos_ejemplo():
    return [
        Producto(1, "Laptop", Decimal('999.99'), 10, "Electrónicos"),
        Producto(2, "Mouse", Decimal('29.99'), 20, "Accesorios"),
        Producto(3, "Teclado", Decimal('59.99'), 15, "Accesorios")
    ]

@pytest.fixture
def tienda_con_productos(tienda, productos_ejemplo):
    for producto in productos_ejemplo:
        tienda.agregar_producto(producto)
    return tienda

def test_agregar_producto_nuevo(tienda):
    # Arrange
    producto = Producto(1, "Laptop", Decimal('999.99'), 10, "Electrónicos")
    
    # Act
    resultado = tienda.agregar_producto(producto)
    
    # Assert
    assert resultado["exito"] == True
    assert producto.id in tienda.productos

def test_agregar_producto_duplicado(tienda_con_productos):
    # Arrange
    producto_duplicado = Producto(1, "Laptop", Decimal('899.99'), 5, "Electrónicos")
    
    # Act
    resultado = tienda_con_productos.agregar_producto(producto_duplicado)
    
    # Assert
    assert resultado["exito"] == False
    assert "ya existe" in resultado["mensaje"]

def test_agregar_producto_al_carrito(tienda_con_productos):
    # Arrange
    usuario_id = "usuario1"
    carrito = tienda_con_productos.obtener_carrito(usuario_id)
    producto = tienda_con_productos.productos[1]
    
    # Act
    resultado = carrito.agregar_producto(producto, 2)
    
    # Assert
    assert resultado["exito"] == True
    assert carrito.items[1] == 2

def test_agregar_producto_sin_stock(tienda_con_productos):
    # Arrange
    usuario_id = "usuario1"
    carrito = tienda_con_productos.obtener_carrito(usuario_id)
    producto = tienda_con_productos.productos[1]
    cantidad_excesiva = producto.stock + 1
    
    # Act
    resultado = carrito.agregar_producto(producto, cantidad_excesiva)
    
    # Assert
    assert resultado["exito"] == False
    assert "stock" in resultado["mensaje"]

def test_remover_producto_del_carrito(tienda_con_productos):
    # Arrange
    usuario_id = "usuario1"
    carrito = tienda_con_productos.obtener_carrito(usuario_id)
    producto = tienda_con_productos.productos[1]
    carrito.agregar_producto(producto, 1)
    
    # Act
    resultado = carrito.remover_producto(producto.id)
    
    # Assert
    assert resultado["exito"] == True
    assert producto.id not in carrito.items

def test_calcular_total_carrito(tienda_con_productos):
    # Arrange
    usuario_id = "usuario1"
    carrito = tienda_con_productos.obtener_carrito(usuario_id)
    
    # Limpiamos el carrito por si acaso
    carrito.items.clear()
    
    # Agregamos productos específicos
    mouse = tienda_con_productos.productos[2]    # Mouse a 29.99
    teclado = tienda_con_productos.productos[3]  # Teclado a 59.99
    
    carrito.agregar_producto(mouse, 2)    # 2 Mouse @ 29.99 = 59.98
    carrito.agregar_producto(teclado, 1)  # 1 Teclado @ 59.99 = 59.99
    
    # Act
    total = tienda_con_productos.calcular_total_carrito(usuario_id)
    
    # Calculamos el total esperado
    total_esperado = (mouse.precio * Decimal('2')) + (teclado.precio * Decimal('1'))
    
    # Assert
    print(f"Total calculado: {total}")
    print(f"Total esperado: {total_esperado}")
    print(f"Contenido del carrito: {carrito.items}")
    print(f"Precios de productos: Mouse={mouse.precio}, Teclado={teclado.precio}")
    
    assert total == total_esperado

def test_actualizar_cantidad_carrito(tienda_con_productos):
    # Arrange
    usuario_id = "usuario1"
    carrito = tienda_con_productos.obtener_carrito(usuario_id)
    producto = tienda_con_productos.productos[1]
    carrito.agregar_producto(producto, 1)
    
    # Act
    resultado = carrito.actualizar_cantidad(producto, 3)
    
    # Assert
    assert resultado["exito"] == True
    assert carrito.items[producto.id] == 3

def test_actualizar_cantidad_excede_stock(tienda_con_productos):
    # Arrange
    usuario_id = "usuario1"
    carrito = tienda_con_productos.obtener_carrito(usuario_id)
    producto = tienda_con_productos.productos[1]
    cantidad_excesiva = producto.stock + 1
    
    # Act
    resultado = carrito.actualizar_cantidad(producto, cantidad_excesiva)
    
    # Assert
    assert resultado["exito"] == False
    assert "stock" in resultado["mensaje"]