from proyecto import ma
from ..models import Log, User, Metadata, Password

#Schemas para convertir el objeto generado por SQLALCHEMY A JSON,
#Cada esquema es generado automaticamente por la estructura de los modelos
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:       
        model = User
        include_fk = True


class PasswordSchema(ma.SQLAlchemyAutoSchema):
    class Meta:       
        model = Password
        include_fk = True


class MetadataSchema(ma.SQLAlchemyAutoSchema):
    class Meta:       
        model = Metadata
        include_fk = True



class LogSchema(ma.SQLAlchemyAutoSchema):
    class Meta:       
        model = Log
        include_fk = True