# 05_Identidad_Hasheo (Capa 7 - Seguridad)

Esta capa añade la lógica para manejar usuarios reales de forma segura. No basta con guardar datos; debemos proteger la contraseña.

## Objetivo
Implementar un sistema de registro donde las contraseñas **NUNCA** se guarden como texto plano en la base de datos, utilizando técnicas de hasheo estándar.

## ¿Qué es diferente/nuevo aquí?

*   **Modelo Inteligente (`app/models/usuario.py`)**:
    *   Sustituimos la columna `password` por `password_hash`.
    *   Métodos `set_password(pwd)`: Convierte "123456" en `scrypt:32768:8:1$k...`.
    *   Métodos `check_password(pwd)`: Verifica si la contraseña coincide con el hash.
    *   Uso de `werkzeug.security` (Librería nativa y probada de Flask).

*   **Blueprint de Autenticación (`app/routes/auth.py`)**:
    *   Nueva ruta `/api/auth/register` que usa el modelo inteligente.
    *   Prefijo de URL `/api/auth` definido en el blueprint para mantener orden.
    
## Comandos Útiles

1.  **Inicializar Entorno Virtual**:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

2.  **Instalar Dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Migrar Base de Datos** (Vital porque cambiamos el modelo Usuario):
    *   Nota: Si vienes de la capa 04, quizás debas borrar la tabla antigua o hacer una migración nueva.
    ```bash
    # Si es primera vez en esta capa limpia:
    flask db init
    flask db migrate -m "Agregar password hash"
    flask db upgrade
    ```

4.  **Ejecutar**:
    ```bash
    flask run
    ```
