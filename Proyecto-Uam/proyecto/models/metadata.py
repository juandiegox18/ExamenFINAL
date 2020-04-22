import datetime
from proyecto import db


class Metadata(db.Model):
    ''' El objeto Metadata contiene la estructura de la tabla Log de la base de datos
        hereda de db.Model de SQLALCHEMY'''
    id = db.Column(db.Integer, primary_key=True)
    creationDate = db.Column(db.DateTime, default=datetime.datetime.now)
    updateDate = db.Column(db.DateTime, default=datetime.datetime.now)
    description = db.Column(db.String(30), nullable=False)
    right = db.Column(db.String(50), nullable=False)
    imagePath = db.Column(db.String(50), nullable=False)
    users = db.relationship('User', backref="team")
    logs = db.relationship('Log', backref="team")