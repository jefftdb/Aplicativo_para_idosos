from app import db

class Jogo(db.Model):
    __tablename__ ='jogo'

    id = db.Column(db.Integer, autoincrement = True, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    url_jogo = db.Column(db.String(255),nullable = False)

    def __init__(self,id,nome,url_jogo) -> None:
        self.id = id
        self.nome = nome
        self.url_jogo = url_jogo

  
usuario_jogo = db.Table(
    'usuario_jogo',
    db.Column("users", db.ForeignKey("users.id")),
    db.Column("jogo", db.ForeignKey("jogo.id")),
    )