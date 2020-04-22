import datetime
from proyecto import db

class Log(db.Model):
    ''' El objeto log contiene la estructura de la tabla Log de la base de datos
        con cada una de su llave foranea de la tabla metadata
        hereda de db.Model de SQLALCHEMY , por lo que permite hacer querys a la BD
        al ser instanciado '''
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime,
                     default=datetime.datetime.utcnow())
    log = db.Column(db.JSON, nullable=False)
    team_id = db.Column(db.String(50),
                      db.ForeignKey('metadata.right'),
                      nullable=False)