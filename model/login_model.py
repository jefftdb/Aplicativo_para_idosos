from app import db,login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from model.video_model import usuario_lista_favorito
from model.jogo_model import usuario_jogo




@login_manager.user_loader
def get_user(user_id):
    return User.query.filter_by(id=user_id).first()

class User (db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, autoincrement = True, primary_key=True)
    nome = db.Column(db.String(86), nullable=False)
    email = db.Column(db.String(84), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    listas_favoritas = db.relationship('Lista_favorito', secondary=usuario_lista_favorito, backref=db.backref('usuarios', lazy='dynamic'))
    listas_jogo = db.relationship('Jogo', secondary=usuario_jogo, backref=db.backref('usuarios', lazy='dynamic'))

    def __init__(self,nome,email,password) -> None:        
        self.nome = nome
        self.email = email       
        self.password = generate_password_hash(password)
        
    def verify_password(self,pwd):
        return check_password_hash(self.password,pwd)
    
    def get_listas_favoritas(self):
        return self.listas_favoritas
    
    