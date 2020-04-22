from proyecto import db
from flask_login import current_user
from ..models.metadata import Metadata
from ..schemas import MetadataSchema
from ..services.log_service import save_log
import datetime

#metodo para guarda un equipo(Metadata) en la base de datos
def save_team(team):
    new_team = Metadata(description=team["description"], right=team["right"], imagePath=team["imagePath"])
    db.session.add(new_team)
    db.session.commit()
    action = f'Saved team {team["description"]}'
    save_log(action, current_user.id, current_user.team)
    msg = "Team created successfully"
    return msg

#metodo para editar un equipo(Metadata)
def update_team(id,description, right, imagePath):
    team = Metadata.query.get(id)
    team.description = description
    team.right = right
    team.imagePath = imagePath
    date = datetime.datetime.now()
    team.updateDate = date
    db.session.commit()
    action = f'Updated team {description}'
    save_log(action, current_user.id, current_user.team)

    msg = "Team updated succesfully"
    return msg

#metodo para obtener los equipos y convertirlos a JSON con los schemas
def get_teams():
    metadata_schema = MetadataSchema(many=True)
    teams = Metadata.query.all()
    result = metadata_schema.dump(teams)
    return result

#metodo para obtener un equipo y convertirlo a JSON con los schemas
def get_team(id):
    metadata_schema = MetadataSchema()
    team = Metadata.query.get(id)
    result = metadata_schema.dump(team)
    return result

#Este metodo permite obtener todos los rights de la tabla Metadatata
def get_all_rights():
    teams =   get_teams()
    rights = []
    for team in teams:
        rights.append(team["right"])
    return rights