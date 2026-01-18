# Contexto del Proyecto: El Código Maestro

Este repositorio documenta mi viaje de aprendizaje para construir un **Backend Maestro**: un código versátil, minimalista y optimizado que sirva como base universal para futuros proyectos, pruebas técnicas o entrevistas.

## Filosofía
El objetivo NO es tener una aplicación con lógica de negocio específica, sino un **arquetipo de infraestructura** perfecto.
Busco:
1.  **Minimalismo**: Solo lo necesario para la etapa actual. Evitar el "code boilerplate" que no se usa (e.g., configuraciones de producción prematuras).
2.  **Carga Cognitiva Baja**: El código debe ser fácil de memorizar, entender y replicar mentalmente.
3.  **Versatilidad**: Una base sólida sobre la cual se puedan construir "Capas" adicionales (Auth, DB, Sockets, etc.).
4.  **Evolución Justificada**: Cualquier cambio en la arquitectura debe tener una justificación clara de por qué es más óptimo o simple que la versión anterior.

## Historia de las Versiones (Backends)

## Arquitectura del Repositorio
El repositorio se ha reorganizado para reflejar la evolución limpia del código. Todos los proyectos se encuentran dentro de la carpeta `backend/`.

*   **`00_Modelo_Legacy` (Antes `backend`)**:
    *   Fue el primer intento. Funcional, pero "sucio". Sirve de referencia histórica.

*   **`01_Arranque_Manual` (Antes `backend3`)**:
    *   Optimización manual.
    *   **Enfoque**: "Solo crea lo que necesitas". Arranque con `python run.py`.

*   **`02_Flask_Basico` (Antes `backend4`)**:
    *   **El Estándar**: Migración a `flask run` y `.flaskenv`. Estructura limpia y configuración mínima.

*   **`03_Rutas_Blueprints` (Antes `backend5`)**:
    *   **Capa de Enrutamiento**: Introducción de `Blueprints` para modularizar las rutas fuera de `__init__.py`.

*   **`04_Base_Datos` (Antes `backend6`)**:
    *   **Capa de Persistencia**: Integración de SQLAlchemy, Extensiones y Migraciones (PostgreSQL).

## Metodología: Las Capas

El desarrollo no es monolítico, es a través de **CAPAS**.
Una "Capa" es un segmento lógico de funcionalidad que se agrega al Código Maestro.
*   *Ejemplo Capa 1*: Levantar el Servidor (Hello World).
*   *Ejemplo Capa 2*: Enrutamiento y Estructura (Blueprints).
*   *Ejemplo Capa 3*: Datos y Migraciones.

**Regla de Oro**: No avanzamos a la siguiente capa hasta que la actual esté entendida, optimizada y justificada.
