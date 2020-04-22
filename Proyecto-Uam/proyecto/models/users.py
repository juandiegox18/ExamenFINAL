from proyecto import db, login_manager
from flask_login import UserMixin

class User(UserMixin, db.Model):
    ''' El objeto log contiene la estructura de la tabla Log de la base de datos
    con cada una de su llave foranea de la tabla metadata 
    hereda de db.Model de SQLALCHEMY , por lo que permite hacer querys a la BD
    al ser instanciado '''
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    right = db.Column(db.String(50),
                      db.ForeignKey('metadata.right'),
                      nullable=False)
    passwords = db.relationship('Password', backref="user", uselist=False)

    @login_manager.user_loader
    def load_user(user_id):
        if user_id is not None:
            user = User.query.get(user_id)
            return user
        return None
