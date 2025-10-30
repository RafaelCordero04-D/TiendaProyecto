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

3. **Crea un entorno virtual
   
   #bash
   ```bash 
   python -m venv venv

5. Activalo
   
   -En windows:
   ```bash
   source .venv/Scripts/activate
   ```
   -En Linux\Mac:
   ```bash
   source venv/bin/activate
   ```
6. Instala las dependencias
   
   #bash
   ```bash
   pip install -r requirements.txt
   ```
8. Ejecutar el servidor
   
   #bash
    ```bash
    uvicorn main:app --reload
    ```
10. Abre tu navegador
  -Documentación interactiva (Swagger UI):
    👉 http://127.0.0.1:8000/docs
   
   
