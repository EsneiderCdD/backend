from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Inicializamos "db" SIN asociarla a la app todavía.
db = SQLAlchemy()
migrate = Migrate()
