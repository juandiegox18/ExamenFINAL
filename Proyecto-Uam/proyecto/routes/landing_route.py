from flask_restful import Resource
from flask_login import login_required
from flask import Response, request, render_template, make_response, render_template

#landing endpoint
class LandingApi(Resource):
    @login_required
    def get(self):
        '''Retorna el template con el index'''
        return make_response(render_template("index.html"))