from datetime import datetime
from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
class Usuario(db.Model): 
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    role = db.Column(db.String(80), nullable=False, default='admin')
    password_hash = db.Column(db.String(250), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f"<Usuario {self.name}>"