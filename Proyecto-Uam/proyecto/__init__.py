from flask import Flask, request
from flask_restful import Api, reqparse
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow
from flask_login import LoginManager
import werkzeug

app = Flask(__name__)

UPLOAD_FOLDER = '/static/images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #Evita que se muestre advertencia
app.config['SECRET_KEY'] = 'ASDASDD'

UPLOAD_FOLDER = 'static/img'

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app) #Se inicializa el ORM

bcrypt = Bcrypt(app) #permite generar hashs

ma = Marshmallow(app) #permite convertir objetos generados por SQLALCHEMY EN JSON

parser = reqparse.RequestParser()
parser.add_argument('file',type=werkzeug.datastructures.FileStorage, location='files')

login_manager = LoginManager()
login_manager.login_view = "loginapi"

login_manager.init_app(app)

api = Api(app)

from .routes import initialize_routes

initialize_routes(api) #Se inicializan las rutas de la aplicacion

