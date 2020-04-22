from proyecto import db, bcrypt
from proyecto.models import User, Password, Metadata, Log

def init_database():
    '''Funcion que crea la BD de acuerdo a los modelos presentes en el proyecto
        y crea registros iniciales '''
    db.create_all() #Se crea la base de datos
    new_meta = Metadata(description="lead01", right="Lead", imagePath="src")
    new_meta2 = Metadata(description="Admin01", right="Admin", imagePath="src")
    new_user = User(username="dbolanos", team=new_meta)
    new_user2 = User(username="jgutierrez", team=new_meta)
    new_user3 = User(username="admin", team=new_meta2)
    password = bcrypt.generate_password_hash("pass1234")
    password2 = bcrypt.generate_password_hash("pass123456")
    new_password = Password(pwd=password, question="Favorite color", answer="blue", user=new_user)
    new_password2 = Password(pwd=password, question="Favorite color", answer="red", user=new_user2)
    new_password3 = Password(pwd=password2, question="Favorite color", answer="yellow", user=new_user3)
    new_log = Log(log="new log", team=new_meta)
    #Se crean nuevos objetos para almacenar en la base de datos
    db.session.add(new_meta)
    db.session.add(new_meta2)
    db.session.add(new_user)
    db.session.add(new_user2)
    db.session.add(new_user3)
    db.session.add(new_password)
    db.session.add(new_password2)
    db.session.add(new_password3)          
    db.session.add(new_log)
    #Se añade cada objeto a la sesion para almacenarlos a la BD
    db.session.commit()
    #Se guardan los datos en la BD
    print("Database Created")

init_database()
