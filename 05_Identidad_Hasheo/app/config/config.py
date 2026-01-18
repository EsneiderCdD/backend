import os

class Config:
    # SQLALCHEMY_DATABASE_URI: La cadena de conexión a la base de datos
    # SQLALCHEMY_TRACK_MODIFICATIONS: Desactiva una funcionalidad pesada que no necesitamos
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
