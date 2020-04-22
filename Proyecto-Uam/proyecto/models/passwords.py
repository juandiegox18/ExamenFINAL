from proyecto import db, bcrypt


class Password(db.Model):
    ''' El objeto Password contiene la estructura de la tabla Log de la base de datos
        hereda de db.Model de SQLALCHEMY, por lo que permite hacer querys a la BD
        al ser instanciado'''
    id = db.Column(db.Integer, primary_key=True)
    pwd = db.Column(db.String(30), nullable=False)
    question = db.Column(db.String(50), nullable=False)
    answer = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
