from .landing_route import LandingApi
from .user_routes import UserApi, UsersApi, LoginApi, LogoutApi, RegisterApi, ChangePasswordApi
from .team_routes import TeamApi, TeamsApi, SaveTeamApi
from .log_routes import LogApi, LogsApi

#Inicializacion de las rutas
def initialize_routes(api):
    api.add_resource(LandingApi, '/')
    api.add_resource(UsersApi, '/users')
    api.add_resource(LoginApi, '/login')
    api.add_resource(UserApi, '/user/<id>')
    api.add_resource(TeamsApi, '/teams')
    api.add_resource(SaveTeamApi, '/saveTeam')
    api.add_resource(TeamApi, '/team/<id>')
    api.add_resource(LogsApi, '/logs')
    api.add_resource(RegisterApi, '/register')
    api.add_resource(LogApi, '/log/<id>')
    api.add_resource(LogoutApi, '/logout')
    api.add_resource(ChangePasswordApi, '/myuser/<id>')