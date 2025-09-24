# FastAPI MySQL REST API

Este proyecto es una API RESTful construida con **FastAPI** y **SQLAlchemy**, conectada a una base de datos **MySQL**. Permite la gestión de usuarios con operaciones CRUD y utiliza cifrado para las contraseñas.

---

## Requisitos

- Python 3.10+
- MySQL Server
- pip

---

## Instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/ArielNCC/Python_FastAPI.git
   cd Python_FastAPI
   ```

2. **Crea y activa un entorno virtual (opcional pero recomendado):**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configura las variables de entorno:**
   - Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:
     ```
     DATABASE_URL=mysql+pymysql://usuario:contraseña@localhost:pu/nombre_db
     FERNET_KEY=tu_clave_fernet_generada
     ```
   - Puedes generar una clave Fernet con:
     ```python
     from cryptography.fernet import Fernet
     print(Fernet.generate_key().decode())
     ```

5. **Ejecuta la aplicación:**
   ```bash
   uvicorn app:app --reload
   ```

---

## Endpoints principales

- `GET /users`  
  Lista todos los usuarios.

- `POST /users`  
  Crea un usuario nuevo.  
  **Body:**  
  ```json
  {
    "name": "Nombre",
    "email": "correo@ejemplo.com",
    "password": "tu_contraseña"
  }
  ```

- `GET /users/{id}`  
  Obtiene un usuario por ID.

- `PUT /users/{id}`  
  Actualiza un usuario existente.

- `DELETE /users/{id}`  
  Elimina un usuario.

---

## Documentación interactiva

Una vez ejecutada la app, accede a la documentación automática en:  
- [http://localhost:8000/docs](http://localhost:8000/docs)

---

## requirements.txt

```
fastapi
uvicorn
sqlalchemy
pymysql
python-dotenv
cryptography
```

---

## Notas de seguridad

- No subas tu archivo `.env` al repositorio.
- Las contraseñas se almacenan cifradas usando Fernet.
- Usa un usuario de base de datos con permisos limitados para producción.

---

## Licencia

MIT
