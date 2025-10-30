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


### 🔍 **GET /productos/**

Obtiene todos los productos activos (status = True).

**Filtros opcionales:**

-stock: Filtrar por cantidad exacta.

-precio_min: Precio mínimo.

-precio_max: Precio máximo.

-categoria_id: ID de categoría.


### 🔎 **GET /productos/search**

Busca productos por nombre de categoría (coincidencia parcial, sin distinguir mayúsculas/minúsculas).

**Respuestas:**

-✅ 200 OK: Lista de productos encontrados.

-❌ 404 Not Found: Categoría o productos no encontrados.


### ⚖️ **GET /producto/ActiveOrInactive/**

Lista los productos filtrando por su estado (its_active).


### 🛠️ **PATCH /productoUpdate/{producto_id}**

Actualiza los datos de un producto específico.


### ❌ **DELETE /productoDelete/{producto_id}**

Desactiva un producto (no lo elimina físicamente).

**Respuestas:**

-✅ 200 OK: Producto desactivado.

-❌ 404 Not Found: Producto no existe o ya está inactivo.


### 🔄 **PUT /productoActivate/{producto_id}**

Activa nuevamente un producto previamente desactivado.

**Respuestas:**

-✅ 200 OK: Producto activado.

-❌ 404 Not Found: Producto no existe o ya está activo.


### 🛒 **PUT /producto/comprar/{producto_id}**

Compra o descuenta stock de un producto.

**Validaciones:**

-El producto debe estar activo.

-La cantidad debe ser mayor que 0.

-El stock no puede quedar negativo.

## 🗂️ Funciones principales - Categorías

### 1️⃣ Crear una nueva categoría

**POST /**  

Crea una nueva categoría.

### 2️⃣ Obtener todas las categorías

**GET /categorias**

Devuelve la lista de todas las categorías registradas (activas e inactivas).

### 3️⃣ Inactivar una categoría y sus productos

**DELETE /inactivate/{categoria_id}**

Desactiva una categoría (status = false) y también todos los productos asociados a ella.

**Errores posibles:**

-404: Categoría no encontrada o ya inactiva.

### 4️⃣ Activar una categoría

**PUT /categoriaActivate/{categoria_id}**

Activa una categoría previamente inactiva.

**Errores posibles:**

-404: Categoría no encontrada o ya activa.

### 5️⃣ Obtener solo las categorías activas

**GET /activateCategorias/**

Devuelve todas las categorías cuyo estado es true.

**Errores posibles:**

-404: No se encontraron categorías activas.

### 6️⃣ Actualizar una categoría

**PATCH /categoriaUpdate/{categoria_id}**

Permite modificar parcialmente una categoría existente.

**Errores posibles:**

-404: Categoría no encontrada.


## 📚 Autor
Desarrollado por [Rafael Cordero ✨](https://github.com/RafaelCordero04-D)
