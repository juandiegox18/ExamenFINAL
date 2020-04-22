from flask import Response, request, render_template, jsonify, make_response, redirect, url_for,flash
from flask_login import current_user
from flask_restful import Resource, reqparse
from flask_login import login_required
from ..services.team_service import get_team, get_teams, update_team, save_team, get_all_rights
from ..services.user_service import get_user_team
import werkzeug
from proyecto import parser

#Se crean los endpoints y se hace uso de los metodos post y get llamando al servicio team_service
class TeamsApi(Resource):
    @login_required
    def get(self):
        try:
            if current_user.right == "Admin":
                titulo = "TEAMS"
                teams = get_teams()
                return make_response(render_template('data.html', datos=teams, titulo=titulo))
            else:   
                team = get_user_team(current_user.id)
                return redirect(f'/team/{team.id}')
        except Exception as e:
            return make_response(jsonify(e, 500))  
    #Obtiene los registros de la tabla Metadata por medio del llamado al metodo get_teams()
    #y los muestra en el template data

class TeamApi(Resource):
    @login_required
    def get(self, id):
        try:
            titulo = "TEAM"
            data = get_team(id)
            items = get_all_rights()
            return make_response(render_template('view.html', datos=data, titulo=titulo, items=items))
        except Exception as e:
            return make_response(jsonify(e, 500))
    #Obtiene 1 registro en especifico por un ID de tabla Metadata por medio del llamado al metodo get_team()
    #y lo muestra en el template view
    @login_required
    def post(self, id):
        try:
            description = request.form["description"]
            right = request.form["right"]
            imagePath = request.form["imagePath"]
            msg = update_team(id, description, right, imagePath)
            flash(msg)
            return redirect(url_for('teamsapi')) 
        except Exception as e:
            return make_response(jsonify(e, 500))


class SaveTeamApi(Resource):
    @login_required
    def get(self):
        items = ["Lead", "Lead-View", "Admin", "User"]
        return make_response(render_template('teamform.html', items=items))
    #se obtienen los datos del form o rest api y son guardados en la BD   
    @login_required
    def post(self):
        data = parser.parse_args()
        if data['file'] == "":
            return {
                    'data':'',
                    'message':'No file found',
                    'status':'error'
                    }
        photo = data['file']

        if photo:
            filename = 'your_image.png'
            #photo.save(os.path.join(UPLOAD_FOLDER,filename))
            return {
                    'data':'',
                    'message':'photo uploaded',
                    'status':'success'
                    }
        else:
            team = {}
            team["description"] =  request.form["description"]
            team["right"] = request.form["right"]
            team["imagePath"] = request.form["file"]
            msg = save_team(team)
            flash("msg")
            return redirect(url_for('teamsapi')) 