from datetime import datetime
from flask_restful import Resource
from flask_login import login_required
from ..services.log_service import get_logs, save_log, get_log
from flask import Response, request, render_template, make_response, jsonify

from ..schemas import LogSchema


class LogsApi(Resource):
    @login_required
    def get(self):
        try:
            titulo = "LOGS"
            logs = get_logs()
            return make_response(render_template('data.html', datos=logs, titulo=titulo))
        except Exception as e:
            return make_response(jsonify(e, 500))  
    #obtiene todos los logs por medio del llamado al log_service y los muestra en el
    #template data
class LogApi(Resource):
    @login_required
    def get(self, id):
        try:
            titulo = "LOG"
            log = get_log(id)
            return make_response(render_template('view.html', datos=log, titulo=titulo))
        except Exception as e:
            return make_response(jsonify(e, 500))  
    #obtiene un log en especifico por un ID y lo muestra en el template view