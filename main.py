
from fastapi import FastAPI

# Creamos nuestra aplicación
app = FastAPI()

# Primer endpoint: página de inicio
@app.get("/")
def inicio():
    return {
        "mensaje": "Bienvenido a nuestra API de productos",
        "estado": "Servidor funcionando correctamente"
    }


# Lista de productos almacenados temporalmente
productos = [
    {"id": 1, "nombre": "Monster", "precio": 10000},
    {"id": 2, "nombre": "Doritos", "precio": 9000},
    {"id": 3, "nombre": "Vape", "precio": 66000}
]

# Segundo endpoint: listar todos los productos
@app.get("/productos")
def listar_productos():
    return {
        "total": len(productos),
        "productos": productos
    }


from fastapi import HTTPException

# Tercer endpoint: buscar un producto por su ID
@app.get("/productos/{id}")
def obtener_producto(id: int):
    for producto in productos:
        if producto["id"] == id:
            return producto

    raise HTTPException(
        status_code=404,
        detail="Producto no encontrado"
    )


from pydantic import BaseModel

# Modelo de los datos que recibiremos
class ProductoNuevo(BaseModel):
    nombre: str
    precio: float

# Cuarto endpoint: crear un producto
@app.post("/productos", status_code=201)
def crear_producto(producto: ProductoNuevo):

    nuevo_id = max(
        (p["id"] for p in productos),
        default=0
    ) + 1

    nuevo_producto = {
        "id": nuevo_id,
        "nombre": producto.nombre,
        "precio": producto.precio
    }

    productos.append(nuevo_producto)

    return nuevo_producto


# Quinto endpoint: eliminar un producto por su ID
@app.delete("/productos/{id}")
def eliminar_producto(id: int):
    for producto in productos:
        if producto["id"] == id:
            productos.remove(producto)

            return {
                "mensaje": "Producto eliminado correctamente",
                "producto_eliminado": producto
            }

    raise HTTPException(
        status_code=404,
        detail="Producto no encontrado"
    )

