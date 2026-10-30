# API REST de Productos con FastAPI

## 1. Descripción del proyecto

Esta aplicación es una API REST desarrollada en Python utilizando FastAPI. Permite consultar, registrar y eliminar productos mediante solicitudes HTTP.

Los productos se almacenan temporalmente en una lista de Python, por lo que no es necesario utilizar una base de datos.

## 2. Framework utilizado: FastAPI

FastAPI es un framework de Python utilizado para desarrollar APIs web. Permite crear endpoints mediante decoradores, recibir solicitudes HTTP y devolver respuestas JSON automáticamente.

**Características principales:**
- Fácil creación de endpoints REST.
- Validación de datos mediante Pydantic.
- Generación automática de documentación.
- Manejo de códigos de estado HTTP.
- Compatibilidad con servidores ASGI como Uvicorn.

## 3. Requisitos

- Python 3.10 o superior.
- pip.
- Postman para probar las solicitudes.

## 4. Instalación

Abrir una terminal dentro de la carpeta del proyecto.

Crear un entorno virtual:

```bash
python -m venv .venv
```

Activarlo en Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## 5. Ejecución del servidor

Ejecutar:

```bash
fastapi dev main.py
```

El servidor estará disponible en:

http://127.0.0.1:8000

Documentación interactiva:

http://127.0.0.1:8000/docs

## 6. Endpoints disponibles

| Método | Endpoint | Descripción | Código HTTP |
|---|---|---|---|
| GET | `/` | Mensaje de bienvenida | 200 |
| GET | `/productos` | Listar productos | 200 |
| GET | `/productos/{id}` | Consultar un producto | 200 / 404 |
| POST | `/productos` | Registrar un producto | 201 |
| DELETE | `/productos/{id}` | Eliminar un producto | 200 / 404 |

## 7. Pruebas realizadas con Postman

### GET /

URL: `http://127.0.0.1:8000/`

Respuesta:

```json
{
  "mensaje": "Bienvenido a nuestra API de productos",
  "estado": "Servidor funcionando correctamente"
}
```

Código HTTP: 200 OK.

### GET /productos

URL: `http://127.0.0.1:8000/productos`

Respuesta inicial:

```json
{
  "total": 3,
  "productos": [
    {"id": 1, "nombre": "Monster", "precio": 10000},
    {"id": 2, "nombre": "Doritos", "precio": 9000},
    {"id": 3, "nombre": "Vape", "precio": 66000}
  ]
}
```

Código HTTP: 200 OK.

### GET /productos/2

URL: `http://127.0.0.1:8000/productos/2`

Respuesta:

```json
{
  "id": 2,
  "nombre": "Doritos",
  "precio": 9000
}
```

Código HTTP: 200 OK.

Si el producto no existe, devuelve 404 Not Found.

### POST /productos

URL: `http://127.0.0.1:8000/productos`

En Postman seleccionar Body → raw → JSON.

Datos enviados:

```json
{
  "nombre": "Coca-Cola",
  "precio": 4500
}
```

Respuesta:

```json
{
  "id": 4,
  "nombre": "Coca-Cola",
  "precio": 4500.0
}
```

Código HTTP: 201 Created.

### DELETE /productos/4

URL: `http://127.0.0.1:8000/productos/4`

Respuesta:

```json
{
  "mensaje": "Producto eliminado correctamente",
  "producto_eliminado": {
    "id": 4,
    "nombre": "Coca-Cola",
    "precio": 4500.0
  }
}
```

Código HTTP: 200 OK.

Si el producto no existe, devuelve 404 Not Found.

## 8. Códigos HTTP utilizados

- **200 OK:** solicitud realizada correctamente.
- **201 Created:** producto creado exitosamente.
- **404 Not Found:** producto no encontrado.
- **422 Unprocessable Entity:** datos enviados incorrectos o incompatibles con el modelo esperado.

## 9. Almacenamiento

La aplicación utiliza una lista de Python como almacenamiento temporal. Los productos agregados o eliminados durante la ejecución no se conservan cuando se reinicia el servidor.

## 10. Conclusión

La actividad permitió comprender el funcionamiento de una API REST utilizando FastAPI, implementar diferentes métodos HTTP y comprobar las respuestas JSON mediante Postman.