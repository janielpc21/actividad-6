from dataclasses import dataclass
from typing import List, Dict
from decimal import Decimal

@dataclass
class Producto:
    id: int
    nombre: str
    precio: Decimal
    stock: int
    categoria: str

class Carrito:
    def __init__(self):
        self.items: Dict[int, int] = {}  # producto_id: cantidad
        
    def agregar_producto(self, producto: Producto, cantidad: int) -> dict:
        if cantidad <= 0:
            return {"exito": False, "mensaje": "La cantidad debe ser mayor a 0"}
            
        if producto.stock < cantidad:
            return {"exito": False, "mensaje": "No hay suficiente stock"}
            
        if producto.id in self.items:
            nueva_cantidad = self.items[producto.id] + cantidad
            if nueva_cantidad > producto.stock:
                return {"exito": False, "mensaje": "No hay suficiente stock"}
            self.items[producto.id] = nueva_cantidad
        else:
            self.items[producto.id] = cantidad
            
        return {"exito": True, "mensaje": "Producto agregado al carrito"}
        
    def remover_producto(self, producto_id: int) -> dict:
        if producto_id not in self.items:
            return {"exito": False, "mensaje": "Producto no encontrado en el carrito"}
            
        del self.items[producto_id]
        return {"exito": True, "mensaje": "Producto removido del carrito"}
        
    def actualizar_cantidad(self, producto: Producto, cantidad: int) -> dict:
        if cantidad <= 0:
            return self.remover_producto(producto.id)
            
        if producto.stock < cantidad:
            return {"exito": False, "mensaje": "No hay suficiente stock"}
            
        self.items[producto.id] = cantidad
        return {"exito": True, "mensaje": "Cantidad actualizada"}

class TiendaEcommerce:
    def __init__(self):
        self.productos: Dict[int, Producto] = {}
        self.carritos: Dict[str, Carrito] = {}  # usuario_id: Carrito
        
    def agregar_producto(self, producto: Producto) -> dict:
        if producto.id in self.productos:
            return {"exito": False, "mensaje": "El producto ya existe"}
            
        if producto.precio <= 0:
            return {"exito": False, "mensaje": "El precio debe ser mayor a 0"}
            
        if producto.stock < 0:
            return {"exito": False, "mensaje": "El stock no puede ser negativo"}
            
        self.productos[producto.id] = producto
        return {"exito": True, "mensaje": "Producto agregado exitosamente"}
        
    def obtener_carrito(self, usuario_id: str) -> Carrito:
        if usuario_id not in self.carritos:
            self.carritos[usuario_id] = Carrito()
        return self.carritos[usuario_id]
        
    def calcular_total_carrito(self, usuario_id: str) -> Decimal:
        carrito = self.obtener_carrito(usuario_id)
        total = Decimal('0')
        
        for producto_id, cantidad in carrito.items.items():
            producto = self.productos.get(producto_id)
            if producto:  # Verificamos que el producto exista
                subtotal = producto.precio * Decimal(str(cantidad))  # Convertimos cantidad a Decimal
                total += subtotal
            
        return total.quantize(Decimal('0.01'))  # Redondeamos a 2 decimales