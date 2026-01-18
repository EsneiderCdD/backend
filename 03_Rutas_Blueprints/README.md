# 03_Rutas_Blueprints (Capa 2)

En esta capa introducimos **Blueprints**, la forma estándar de Flask para organizar rutas.

## Arquitectura Actual (Capa 2)
```text
backend5/
├── .flaskenv
├── .env
└── app/
    ├── __init__.py     
    └── routes/          
        ├── __init__.py
        └── main.py    
```

## Objetivo
Organizar las rutas de la aplicación de manera modular y escalable, evitando que el archivo `__init__.py` se convierta en un monolito gigante.

## ¿Qué es diferente/nuevo aquí?
*   **Blueprints**: Introducimos el concepto de "Planos" que nos permite definir rutas en archivos separados (`app/routes/main.py`).
*   **Separación de Responsabilidades**: `__init__.py` solo crea la app y conecta los cables. Las rutas viven en su propia casa.
*   **Prefijos de URL**: Preparación para poder agrupar rutas (ej: `/api/users`, `/api/auth`) fácilmente en el futuro.

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

3.  **Ejecutar Servidor**:
    ```bash
    flask run
    ```
