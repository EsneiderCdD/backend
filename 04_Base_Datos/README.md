# 04_Base_Datos (Capa 3)

Esta capa introduce la conexión robusta a Base de Datos usando el patrón "Extensions".

## Arquitectura Actual (Capa 3)
```text
04_Base_Datos/
├── .flaskenv
├── .env                 <-- AHORA SÍ es vital: Contiene DATABASE_URL
├── app/
│   ├── config/          <-- Carpeta semántica
│   │   └── config.py    <-- Lee DATABASE_URL
│   ├── extensions.py    <-- Inicializa db = SQLAlchemy()
│   ├── __init__.py      <-- Conecta: db.init_app(app)
│   ├── models/
│   │   └── usuario.py
│   └── routes/
│       └── main.py
```

## Objetivo
Conectar la aplicación a una base de datos real (PostgreSQL) de forma profesional, evitando dependencias circulares y permitiendo la evolución de la estructura de datos (migraciones).

## ¿Qué es diferente/nuevo aquí?
*   **Patrón Extensions (`app/extensions.py`)**: Inicializamos `db` fuera de la app para evitar errores de importación circular.
*   **Modelos (`app/models/`)**: Estructura dedicada para definir tablas (ej: `Usuario`).
*   **Configuración Real**: `app/config/config.py` vuelve al juego para leer `DATABASE_URL` desde `.env`.
*   **Flask-Migrate**: Herramienta para gestionar cambios en la base de datos sin tocar SQL manualmente.
## Comandos Útiles (Generales)

1.  **Inicializar Entorno Virtual**:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

2.  **Instalar Dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Ejecutar Servidor**:
    ```bash
    flask run
    ```

## Comandos de Base de Datos (Migraciones)
Al integrar `Flask-Migrate`, ahora gestionamos la base de datos con comandos en lugar de scripts manuales:

1.  **Inicializar repositorio de migraciones** (Solo la primera vez):
    ```bash
    flask db init
    ```
    *Crea la carpeta `migrations` en tu proyecto.*

2.  **Generar una migración** (Cada vez que cambies un modelo):
    ```bash
    flask db migrate -m "Mensaje describiendo el cambio"
    ```
    *Detecta cambios en `app/models` y crea un script SQL automáticamente.*

3.  **Aplicar cambios a la DB**:
    ```bash
    flask db upgrade
    ```
    *Ejecuta los scripts SQL pendientes en tu base de datos PostgreSQL.*
