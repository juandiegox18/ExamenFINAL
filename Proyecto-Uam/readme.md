###Proyecto

el proyecto permite la administracion de usuarios, sus equipos y sus movimientos en el sistema.

###Pasos ejecución
En el directorio de proyecto_uam en la terminal, ejecutar pipenv shell
Luego ejecutar el siguiente comando pipenv install requirements.txt
Despues ejecutar el script de la base de datos de la siguiente manera python scriptbd.py, este retornara por consola que la base de datos ha sido creada
Luego escribir en la terminal python run.py
escribir http://localhost:5000/ en cualquier buscador y este abrirá la aplicacion
los datos de inicio de sesion estan en el script

###Paquetes utilizados
FLASK-LOGIN
FLASK-RESTFUL
FLASK-BCRYPT
FLASK
FLASK-SQLALCHEMY
FLASK-MARSHMALLOW
MARSHMALLOW-SQLALCHEMY
BCRYPT

####Flujo

####Login
El usuario digita su usuario y contraseña e ingresa al sistema

####User management
Permite al usuario cambiar sus datos, contraseñas
Si es administrador podra cambiar los datos de todos los usuarios

####Register
Permite la creacion de un usuario con sus respectivos datos, se genera el hash de la contraseña y se almacenan en la base de datos

####Team management
Se pueden ver los equipos y su informacion del usuario loggeado
Si es admin puede modificar todos los equipos, si no lo es solo podra ver la informacion de su equipo y si es lead la podra modificar

####Logs
Cada cambio en los datos del sistema generara un log con la accion e informacion que ha sido cambiada asi como el usuario que los genero y su equipo
