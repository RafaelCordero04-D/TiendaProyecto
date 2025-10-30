# 🏪 TiendaProyecto

TiendaProyecto es un API REST construida con *FastAPI* que permite gestionar categorias y productos en una Tienda Online.
Incluye operaciones CRUD y una base de datos SQLite para almacenar la información.

-----

## 🚀 Tecnologías usadas
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLModel](https://sqlmodel.tiangolo.com/)
- SQLite
- Pydantic

-----

## ⚙️ Instalación y ejecución

1. **Clona el repositorio**

   #bash
   ```bash
   git clone https://github.com/RafaelCordero04-D/TiendaProyecto.git
   cd TiendaProyecto

2. **Crea un entorno virtual
   
   #bash
   ```bash 
   python -m venv venv

3. Activalo
   
   -En windows:
   ```bash
   source .venv/Scripts/activate
   ```
   -En Linux\Mac:
   ```bash
   source venv/bin/activate
   ```
4. Instala las dependencias
   
   #bash
   ```bash
   pip install -r requirements.txt
   ```
5. Ejecutar el servidor
   
   #bash
    ```bash
    uvicorn main:app --reload
    ```
6. Abre tu navegador
  -Documentación interactiva (Swagger UI):
    👉 http://127.0.0.1:8000/docs

   
## 🧩 Funciones principales- Productos

Estos endpoints permiten gestionar los productos de la tienda.  
Incluyen operaciones de creación, consulta, actualización, activación, compra y eliminación lógica.}

### 🟢 **POST /productos/**
Crea un nuevo producto.

**Validaciones:**
- No se permite un `stock` negativo.
- La categoría debe existir.

**Respuestas**
-✅ 201 Created: Producto creado correctamente.
-❌ 400 Bad Request: Stock negativo o categoría no encontrada.

### 🔍 **GET /productos/

Obtiene todos los productos activos (status = True).

**Filtros opcionales:**

-stock: Filtrar por cantidad exacta.
-precio_min: Precio mínimo.
-precio_max: Precio máximo.
-categoria_id: ID de categoría.

### 🔎 **GET /productos/search

Busca productos por nombre de categoría (coincidencia parcial, sin distinguir mayúsculas/minúsculas).

**Respuestas:**

-✅ 200 OK: Lista de productos encontrados.
-❌ 404 Not Found: Categoría o productos no encontrados.
