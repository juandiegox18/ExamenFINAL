from flask_restful import Resource
from flask_login import login_required, logout_user, current_user, login_user
from flask import Response, request, render_template, jsonify, make_response, flash,redirect, url_for, flash
from ..services.user_service import get_user, get_users, create_user, update_user, delete_user, login, update_my_user
from ..services.team_service import get_all_rights

#Se crean los endpoints y se hace uso de los metodos post y get llamando al servicio user

class UsersApi(Resource):
    @login_required
    def get(self):
        try:
            if current_user.right == "Admin":
                titulo = "USERS"
                data = get_users()
                return make_response(render_template('data.html', datos=data, titulo=titulo))
            else:
                return redirect(f'/user/{current_user.id}')
        except Exception as e:
            return make_response(jsonify(e, 500))
    #los datos se obtienen por el metodo get_users() y se muestran en el template data
    
class RegisterApi(Resource):
    def get(self):
        rights = get_all_rights()
        questions = ["Favorite color", "Favorite place", "Mother's name"]
        return make_response(render_template('Userform.html', questions=questions, items=rights, titulo="REGISTER"), 200)
    
    def post(self):
        try:
            username = request.form["username"]
            password = request.form['password']
            right = request.form['right']
            answer = request.form['answer']
            question = request.form['question']
            msg = create_user(username,password, right, question, answer)
            flash(msg)
            return redirect(url_for('loginapi')) 
        except Exception as e:
            return make_response(jsonify(e, 500))  
    #se obtienen los datos del form o rest api y son guardados en la BD
 
class UserApi(Resource):
    @login_required
    def get(self, id):
        try:
            titulo = "USER"
            items = get_all_rights()
            data = get_user(id, False)
            return make_response(render_template('view.html', datos=data, titulo=titulo, items = items))
        except Exception as e:
            return make_response(jsonify(e, 500))  
    #los datos se obtienen por el metodo get_users() y se muestran en el template data

    @login_required
    def post(self, id):
        try:
            username = request.form["username"]
            right = request.form["right"]
            msg = update_user(id, username, right)
            flash(msg)
            return redirect(url_for('usersapi')) 
        except Exception as e:
            return make_response(jsonify(e, 500))  

class LoginApi(Resource):
    def get(self):
        if current_user.is_authenticated:
            return redirect(url_for('landingapi')) 
        return make_response(render_template('loginform.html'), 200)
    
    def post(self):
        try:
            username = request.form["username"]
            password = request.form['password']
            msg = login(username, password)
            flash(msg)
            return redirect(url_for('landingapi')) 
        except Exception as e:
            return make_response(jsonify(e, 500))  

class LogoutApi(Resource):
    @login_required
    def get(self):
        logout_user()
        flash("Logout successfully")
        return redirect(url_for('loginapi')) 

class ChangePasswordApi(Resource):
    @login_required
    def get(self, id):
        data = get_user(id, True)
        return make_response(render_template("password.html", datos=data))
    @login_required
    def post(self, id):
        try:
            username = request.form["username"]
            password = request.form['password']
            answer = request.form['answer']
            question = request.form['question']
            msg = update_my_user(current_user.id, username, password,question, answer)
            flash(msg)
            return redirect(url_for('landingapi')) 
        except Exception as e:
            return make_response(jsonify(e, 500))

#TODO FLash messages  