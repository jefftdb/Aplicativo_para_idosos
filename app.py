from flask import Flask
import os
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__, template_folder=os.path.abspath('view/templates'), static_folder=os.path.abspath("view/static"))

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost/idosos'

app.config['SECRET_KEY'] = 'secret'

UPLOAD_FOLDER = "./view/static/data"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000



login_manager = LoginManager(app)
db = SQLAlchemy(app)
migrate = Migrate(app,db)
from controller.login_controller import *
from controller.lista_videos_controller import *

if __name__ == "__main__":
    app.run()