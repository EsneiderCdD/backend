# 01_Arranque_Manual (Capa Inicial)

Esta capa representa la forma manual de levantar un servidor Flask. Aunque usamos Flask como librería, la gestión del proceso se hace "desde afuera" con scripts propios de Python.

## Arquitectura
```text
backend3/
├── .env
├── run.py
├── app/
│   ├── __init__.py
│   └── config/
│       └── config.py
```

## Objetivo
Entender cómo levantar un servidor Flask "a mano", gestionando nosotros mismos la carga de variables de entorno y el punto de entrada de la aplicación.

## ¿Qué es diferente/nuevo aquí?
*   **Arranque Manual**: Usamos `python run.py` en lugar de comandos automáticos.
*   **Configuración Explícita**: El modo Debug se define en código (`DEBUG=True`).
*   **Gestión de Entorno**: Importamos `dotenv` manualmente en el código.

## Comandos Útiles

1.  **Inicializar Entorno Virtual**:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # Windows
    ```

2.  **Instalar Dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Ejecutar Servidor**:
    ```bash
    python run.py
    ```

4.  **Guardar nuevas dependencias**:
    ```bash
    pip freeze > requirements.txt
    ```
