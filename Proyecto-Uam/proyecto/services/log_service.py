import json
from flask_login import current_user
from proyecto import db, login_manager
from ..models import Log, User
from ..schemas import LogSchema


def save_log(action, user, team_id):
    '''
        Metodo para crear un log y guardarlo en la base dedatos
        Recibe el log nuevo por parametros inicializa el modelo Log y lo guarda en la BD
    '''
    log = {
        'action': action,
        'user': user
    }
    json_log = json.dumps(log)
    new_log = Log(log=json_log, team=team_id)
    db.session.add(new_log)
    db.session.commit()
    return True

def get_logs():
    '''
        Funcion para obtener los registros almacenados en la tabla Log
        los mismos son convertidos por el schema LogSchema y son retornados
    '''
    if current_user.right == "Admin" or current_user.right == "Lead-View":
        log_schema = LogSchema(many=True)
        logs = Log.query.all()
        result = log_schema.dump(logs)
        return result
    elif current_user.right == "Lead":
        log_schema = LogSchema(many=True)
        logs = Log.query.filter_by(team_id=current_user.right)
        result = log_schema.dump(logs)
        return result

def get_log(id):
    '''
        Funcion para obtener un registro almacenado en la tabla Log por un ID
        en especifico
        convertido por el schema LogSchema y son retornado
    '''
    log_schema = LogSchema()
    log = Log.query.get(id)
    result = log_schema.dump(log)
    return result