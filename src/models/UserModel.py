import enum
from pydantic import BaseModel, Field
from typing import Optional,List,Dict
from ..models.HorarioModel import Horario, Horario_Default_Response
from ..models.EquipoModel import Equipo, Equipo_Default_Response

class TipoEnum(str, enum.Enum):
    admin = "Admin"
    normal = "Normal"
    jefe = "Jefe"
    
    
class User(BaseModel):
    id_usuario: int
    tipo: TipoEnum
    nombre: str
    email: str
    password: str
    id_equipo: Optional[int] = Field(default=None)
    
def User_Default_Response(results: List[tuple]) -> List[User]:
    return [User(**dict(zip(("id_usuario", "tipo", "nombre", "email", "password", "id_equipo"), row))) for row in results]
    

class UserDetails(BaseModel):
    id_usuario: int
    tipo: TipoEnum
    nombre: str
    email: str
    password: str
    id_equipo: Optional[int] = Field(default=None)
    equipo: Optional[List[Equipo]] = Field(default=None)
    horarios: Optional[List[Horario]] = Field(default=None)
    
class UserBasicDetails(BaseModel):
    id_usuario: int
    tipo: TipoEnum
    nombre: str
    email: str
    password: str
    id_equipo: Optional[int] = Field(default=None)
    # equipo: Optional[List[Equipo]] = Field(default=None)
    horarios: Optional[List[Horario]] = Field(default=None)    
    


def User_Details_Response(user_results: List[tuple]) -> List[UserBasicDetails]:
    user_details_list: List[UserBasicDetails] =  []
    horarios_data = []
    for row in user_results:
        # Descomponer la fila en un diccionario
        row_dict = dict(zip(
            ("id_usuario", "tipo", "nombre", "email", "password", "id_equipo",
             "id_usuario_h","id_horario", "fecha", "hora_inicio", "hora_fin"), row))
        
        # Obtener o crear el objeto UserDetails
        id_usuario = row_dict["id_usuario"]
        
        if not any(user.id_usuario == id_usuario for user in user_details_list):
            user_details_list.append(UserBasicDetails(
                id_usuario=id_usuario,
                tipo=row_dict["tipo"],
                nombre=row_dict["nombre"],
                email=row_dict["email"],
                password=row_dict["password"],
                id_equipo=row_dict["id_equipo"],
                horarios=[]  # Inicializar como lista vacía
            ))
        
        horarios = extraer_horarios(row_dict, horarios_data)

    # Asignar los horarios a cada UserDetails
    for user in user_details_list:
        user.horarios = [h for h in horarios if h.id_usuario == user.id_usuario]
    
    # Retornar la lista de UserDetails
    return user_details_list


def extraer_equipos(row_dict, equipos_data):
    # Solo agregar si el equipo no está ya en equipos_data
    if row_dict["id_equipo"] is not None:
        # Verifica si el id_equipo ya está en equipos_data
        if not any(equipo[0] == row_dict["id_equipo_e"] for equipo in equipos_data):
            equipos_data.append((
                row_dict["id_equipo_e"],
                row_dict["tipo_e"],
                row_dict["nombre_e"],
                row_dict["horas_inicio_act"],
                row_dict["horas_fin_act"]
            ))
            
    # Convertir los horarios a objetos Horario usando el método Horario_Default_Response
    equipos = Equipo_Default_Response(equipos_data)
    return equipos

def extraer_horarios(row_dict, horarios_data):
    # Agregar el horario correspondiente a la lista
    if row_dict["id_horario"] is not None:
            horarios_data.append((row_dict["id_usuario_h"],
                                  row_dict["id_horario"], 
                                  row_dict["fecha"], 
                                  row_dict["hora_inicio"], 
                                  row_dict["hora_fin"]))
            
    # Convertir los horarios a objetos Horario usando el método Horario_Default_Response
    horarios = Horario_Default_Response(horarios_data)
    return horarios

def User_All_Info_Response(user_results: List[tuple]) -> List[UserDetails]:
    user_details_list: List[UserDetails] = []
    horarios_data = []
    equipos_data = []

    for row in user_results:
        # Descomponer la fila en un diccionario
        row_dict = dict(zip(
            ("id_usuario", 
             "tipo", 
             "nombre", 
             "email", 
             "password", 
             "id_equipo",
             "id_equipo_e",
             "tipo_e",
             "nombre_e",
             "horas_inicio_act", 
             "horas_fin_act",
             "id_usuario_h",
             "id_horario", 
             "fecha", 
             "hora_inicio", 
             "hora_fin"), row))
        
        # Check if user already exists in user_details_list
        user = next((u for u in user_details_list if u.id_usuario == row_dict["id_usuario"]), None)
        
        if user is None:
            # If not, create a new UserDetails and add it to the list
            user = UserDetails(
                id_usuario=row_dict["id_usuario"],
                tipo=row_dict["tipo"],
                nombre=row_dict["nombre"],
                email=row_dict["email"],
                password=row_dict["password"],
                id_equipo=row_dict["id_equipo"],
                equipo=[],
                horarios=[]
            )
            user_details_list.append(user)

        # Add team and schedule data
        equipos = extraer_equipos(row_dict, equipos_data)
        horarios = extraer_horarios(row_dict, horarios_data)

    # Assign the equipos and horarios to each user
    for user in user_details_list:
        user.equipo = [equipo for equipo in equipos if equipo.id_equipo == user.id_equipo]
        user.horarios = [h for h in horarios if h.id_usuario == user.id_usuario]

    return user_details_list
