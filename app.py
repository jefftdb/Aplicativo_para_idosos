from flask import Flask
import os
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder=os.path.abspath('view/templates'), static_folder=os.path.abspath("view/static"))

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost/idosos'
app.config['SECRET_KEY'] = 'secret'


login_manager = LoginManager(app)
db = SQLAlchemy(app)

from controller.login_controller import *
from controller.lista_videos_controller import *

if __name__ == "__main__":
    app.run(debug=True)