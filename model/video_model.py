from model.login_model import User
from app import db

class Categoria(db.Model):
    __tablename__ = 'categoria'
    id = db.Column(db.Integer, autoincrement = True, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

    def __init__(self,id,nome) -> None:
        self.id = id
        self.nome = nome
    
    def get_categoria(self):
        return Categoria.query.all()
    
class Lista_videos(db.Model):
    __tablename__ = 'lista_videos'
    id = db.Column(db.Integer, autoincrement = True, primary_key=True)
    url_lista = db.Column(db.String(255),nullable = False)
    titulo = db.Column(db.String(255),nullable = False)
    id_user = db.Column(db.Integer, db.ForeignKey("users.id"))
    id_categoria = db.Column(db.Integer, db.ForeignKey("categoria.id"))

    def get_lista_videos(self):
        return Lista_videos.query.all()

class Video(db.Model):
    __tablename__ = 'video'
    id = db.Column(db.Integer, autoincrement = True, primary_key=True)
    titulo = db.Column(db.String(255),nullable = False)
    url_video = db.Column(db.String(255),nullable = False)
    id_lista = db.Column(db.Integer, db.ForeignKey("lista_videos.id"))

class Lista_favorito(db.model):
    __tablename__ = 'lista_favorito'
    id = db.Column(db.Integer, autoincrement = True, primary_key=True)
    url_lista = db.Column(db.String(255),nullable = False)
    titulo = db.Column(db.String(255),nullable = False)

usuario_lista_favorito = db.Table(
    'usuario_lista_favorito',
    db.Column("users", db.ForeignKey("users.id")),
    db.Column("lista_favorito", db.ForeignKey("lista_favorito.id")),
    )