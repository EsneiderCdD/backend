# 02_Flask_Basico (Capa 1)

Esta capa marca la transición hacia el "Modo Flask". Eliminamos el código boilerplate de arranque y delegamos esa responsabilidad a la herramienta de línea de comandos de Flask.

## Arquitectura Actual (Capa 1)
```text
backend4/
├── .flaskenv
├── .env
└── app/
    └── __init__.py
```

## Objetivo
Migrar al ecosistema nativo de Flask ("The Flask Way") para reducir código innecesario y errores de configuración manual.

## ¿Qué es diferente/nuevo aquí?
*   **Arranque Nativo (`flask run`)**: Reemplaza a `python run.py`.
*   **Archivo `.flaskenv`**: Centraliza la configuración del entorno (puerto, debug) fuera del código.
*   **Limpieza**: Eliminación de boilerplate. `config.py` y `run.py` desaparecen porque Flask CLI asume esas responsabilidades.

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

3.  **Ejecutar Servidor** (La magia de Flask CLI):
    ```bash
    flask run
    ```
    *Lee automáticamente `.flaskenv`.*

4.  **Guardar nuevas dependencias**:
    ```bash
    pip freeze > requirements.txt
    ```
