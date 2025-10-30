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

   ```bash
   git clone https://github.com/RafaelCordero04-D/TiendaProyecto.git
   cd TiendaProyecto

2. **Crea un entorno virtual
   ```bash 
   python -m venv venv

3. Activalo
   
   #En windows:
   ```bash
   source .venv/Scripts/activate
   ```
   #En Linux\Mac:
   ```bash
   source venv/bin/activate
   ```
5. Insala las dependencias
   ```bash
   pip install -r requirements.txt
   ```
6. Ejecutar el servidor
    ```bash
    uvicorn main:app --reload
    ```
7. Abre tu navegador
  -Documentación interactiva (Swagger UI):
    👉 http://127.0.0.1:8000/docs
   
   
