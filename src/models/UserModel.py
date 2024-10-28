from pydantic import BaseModel, Field
from typing import Optional,List,Tuple,Dict
from ..models.HorarioModel import Horario, Horario_Default_Response

class User(BaseModel):
    id_usuario: int
    tipo: str
    nombre: str
    email: str
    password: str
    id_equipo: Optional[int] = Field(default=None)
    
def User_Default_Response(results: List[tuple]) -> List[User]:
    return [User(**dict(zip(("id_usuario", "tipo", "nombre", "email", "password", "id_equipo"), row))) for row in results]
    user = []
    for row in results:
        user.append(User(id_usuario=row[0], 
                         tipo=row[1], 
                         nombre=row[2], 
                         email=row[3], 
                         password=row[4], 
                         id_equipo=row[5] if row[5] is not None else None))
    return user

class UserDetails(BaseModel):
    id_usuario: int
    tipo: str
    nombre: str
    email: str
    password: str
    id_equipo: Optional[int] = Field(default=None)
    # equipo: Optional[str] = Field(default=None)
    horarios: Optional[List[Horario]] = Field(default=None)
    
    


def User_Details_Response(user_results: List[tuple]) -> List[UserDetails]:
    user_details_dict: Dict[int, UserDetails] = {}
    horarios_data = []

    for row in user_results:
        # Descomponer la fila en un diccionario
        row_dict = dict(zip(
            ("id_usuario", "tipo", "nombre", "email", "password", "id_equipo", 
             "id_horario", "fecha", "hora_inicio", "hora_fin"), row))
        
        # Obtener o crear el objeto UserDetails
        id_usuario = row_dict["id_usuario"]
        
        if id_usuario not in user_details_dict:
            user_details_dict[id_usuario] = UserDetails(
                id_usuario=id_usuario,
                tipo=row_dict["tipo"],
                nombre=row_dict["nombre"],
                email=row_dict["email"],
                password=row_dict["password"],
                id_equipo=row_dict["id_equipo"],
                horarios=[]  # Inicializar como lista vacía
            )
        
        # Agregar el horario correspondiente a la lista
        if row_dict["id_horario"] is not None:
            horarios_data.append((row_dict["id_horario"], id_usuario, row_dict["fecha"], row_dict["hora_inicio"], row_dict["hora_fin"]))

    # Convertir los horarios a objetos Horario usando el método Horario_Default_Response
    horarios = Horario_Default_Response(horarios_data)

    # Asignar los horarios a cada UserDetails
    for user in user_details_dict.values():
        user.horarios = [h for h in horarios if h.id_usuario == user.id_usuario]
    
    # Retornar la lista de UserDetails
    return list(user_details_dict.values())




