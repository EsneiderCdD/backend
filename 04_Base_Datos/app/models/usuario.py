from app.extensions import db

class Usuario(db.Model):
    # Definimos la tabla 'usuarios'
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    
    def __repr__(self):
        return f'<Usuario {self.username}>'
