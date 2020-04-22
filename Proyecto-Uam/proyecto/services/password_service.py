from proyecto import bcrypt
from proyecto import db
from ..models.passwords import Password

#Metodo para validar la contraseña
def validate_password(password, msg):
    if len(password) < 6:
        msg = "Password must be more than 6 characters"
        return msg  
    if len(password) > 20:
        msg = "Password must be less than 20 characters"
        return msg  
    if not any(char.isdigit() for char in password): 
        msg = "Password must contain numbers"
        return msg  
    if not any(char.isalpha() for char in password):
        msg = "Password must contain letters"
        return msg  
    else:
        return msg  

#metodo para crear el hash de la contraseña
def hash_password(password):
    hashed = bcrypt.generate_password_hash(password)
    return hashed

#metodo para comparar la contraseña enviada por el usuario con el hash
def check_password(hashed_password, password):
    checked = bcrypt.check_password_hash(hashed_password, password)
    return checked
    
#metodo para cambiar la contraseña
def change_password(user_id, password, question, answer, msg):
    pwd = Password.query.filter(user_id=user_id)
    if pwd:
        if pwd.answer == answer and pwd.question == question:
            pwd.password = hash_password(password)
            db.session.commit()
            msg = "password updated"
            return msg
        else: 
            msg = "Answer or question are incorrect"
            return msg
    else:
        msg = "The given user has no password"
        return msg


'''TODO Que no se repita el mismo carácter dos veces 
seguidas y que evalúe que contenga tanto caracteres como números'''