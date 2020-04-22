from proyecto import db, login_manager
from flask import flash
from flask_login import login_user, current_user
from ..models import User, Metadata, Password
from ..services.password_service import validate_password, check_password, hash_password
from ..schemas import UserSchema, PasswordSchema, MetadataSchema
from ..services.log_service import save_log

#Valida que los datos del usuario ingresado sean correctos
def validate_user(username, password, right):
    if password and username and right:
        return True
    else:
        return False

#valida que el nombre de usuario no exista ya en la base de datos
def user_exists(username):
    user = db.session.query(User).filter(User.username == username).first()
    if user:
        return True
    else:
        return False

#obtiene los usuarios y los convierte a json usando el schema
def get_users():
    user_schema = UserSchema(many=True)
    users = User.query.all()
    if users:
        result = user_schema.dump(users)
        return result
    else:
        flash("No users found")

#obtiene un usuario y lo convierte a json usando el schema
def get_user(id, act):
    if act: 
        user = User.query.get(id)
        return user
    else:
        user_schema = UserSchema()
        user = User.query.get(id)
        result = user_schema.dump(user)
        return result

#Metodo para crear un usuario validando sus campos y que no sea ya existente en la BD
def create_user(username, password, right, question, answer):
    if validate_user(username, password, right):
        msg = ""
        if not user_exists(username):
            msg = validate_password(password, msg)
            if msg == "": 
                team = db.session.query(Metadata).filter(Metadata.right==right).first()
                password = hash_password(password)
                new_user = User(username=username, team=team)
                new_password = Password(pwd=password, question=question, answer=answer, user=new_user)
                db.session.add(new_user)
                db.session.add(new_password)
                db.session.commit()
                action = f'Saved User {username}'
                save_log(action, username, team)
                msg = "User created successfully"
                return msg
            else: 
                return msg
        else:
            msg = "Given username is already in use"
            return msg
    else:
        msg = "Invalid User"
        return msg

#metodo para actualizar un usuario validando que el  mismo exista
def update_my_user(id,username, password, question, answer):
    user = User.query.get(id)
    if user:
        if username and password and question and answer:
            user.username = username
            if check_password(user.passwords.pwd, password):
                db.session.commit()
                return "User updated successfully"
            else:
                if user.passwords.answer == answer:
                    user.passwords.pwd = hash_password(password)
                    db.session.commit()
                    action = f'Updated User {username}'
                    save_log(action, current_user.id, current_user.team)
                    return "User updated successfully"
                else: 
                    return "Invalid answer"               
        else:
            msg = "Invalid data"
            return msg 
    else:
        msg = "User does not exist"
        return msg

#metodo para borrar un usuario
def delete_user(id, msg):
    user = user = User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
    else:
        msg = "User does not exist"
        return msg

#Metodo para efectuar el login en el sistema
#por medio de Flask_login
def login(username, password):
    if username and password:
        user = db.session.query(User).filter_by(username=username).first()
        if user:
            if user.passwords:
                if check_password(user.passwords.pwd, password):
                    login_user(user)
                    return "Logged in"
            else: 
                return "wrong username or password"
        else: 
            return "Invalid user or password"
    else:
        return "Invalid data"

def get_user_team(id):
    user = db.session.query(User).get(id)
    if user:
        return user.team
    else:
        flash("No users found")

#metodo para actualizar un usuario validando que el  mismo exista
def update_user(id,username, right):
    user = User.query.get(id)
    if user:
        if username and right:
            team = db.session.query(Metadata).filter(Metadata.right==right).first()
            user.username = username
            user.team = team
            db.session.commit()
            action = f'Updated User {username}'
            save_log(action, current_user.id, current_user.team)
            return "User updated successfully"
        else:
            msg = "Invalid data"
            return msg 
    else:
        msg = "User does not exist"
        return msg
