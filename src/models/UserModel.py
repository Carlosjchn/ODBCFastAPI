import enum
from pydantic import BaseModel, Field
from typing import Optional, List
from ..models.HorarioModel import Horario, Horario_Default_Response
from ..models.EquipoModel import Equipo, Equipo_Default_Response
from .helpers.user.UserModelHelper import extraer_equipos, extraer_horarios
from .helpers.user.UserDetailsHelper import resultsDetail_to_dict, initUserDetailsModel, asignarHorarios
from .helpers.user.UserAllInfoHelper import results_allDetails_to_dict, check_existing_user, init_UserAllDetails_model, assing_byId

class TipoEnum(str, enum.Enum):
    admin = "Admin"
    normal = "Normal"
    jefe = "Jefe"


###############
# MODELO BASE #
###############


class User(BaseModel):
    id_usuario: int
    tipo: TipoEnum
    nombre: str
    email: str
    password: str
    id_equipo: Optional[int] = Field(default=None)


# Metodo para pasar de Objeto a String.
def User_Default_Response(results: List[tuple]) -> List[User]:
    return [
        User(
            **dict(
                zip(
                    ("id_usuario", "tipo", "nombre", "email", "password", "id_equipo"),
                    row,
                )
            )
        )
        for row in results
    ]


#######################
# MODELO CON HORARIOS #
#######################


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
    user_details_list: List[UserBasicDetails] = []
    horarios_data = []
    
    for row in user_results:
        # Descomponer la fila de los resultados en un diccionario.
        resultsquery_dict = resultsDetail_to_dict(row)
        # Inicializar lista de UserBasicDetails.
        initUserDetailsModel(resultsquery_dict, user_details_list, UserBasicDetails)
        # Inicializar Horarios de cada respuesta.
        horarios = Horario_Default_Response(
            extraer_horarios(resultsquery_dict, horarios_data)
        )
    # Asignar los horarios a cada usuario dentro de UserDetails
    asignarHorarios(user_details_list, horarios)

    # Retornar la lista de UserDetails
    return sorted(user_details_list, key=lambda u: u.id_usuario)


####################
# MODELO DETALLADO #
####################


class UserDetails(BaseModel):
    id_usuario: int
    tipo: TipoEnum
    nombre: str
    email: str
    password: str
    id_equipo: Optional[int] = Field(default=None)
    equipo: Optional[List[Equipo]] = Field(default=None)
    horarios: Optional[List[Horario]] = Field(default=None)


def User_All_Info_Response(user_results: List[tuple]) -> List[UserDetails]:
    user_details_list: List[UserDetails] = []
    horarios_data = []
    equipos_data = []

    for row in user_results:
        # Descomponer la fila en un diccionario
        results_dict = results_allDetails_to_dict(row)
        # Add team and schedule data to the respective data structures
        # Check if user already exists in user_details_list
        if check_existing_user(user_details_list, results_dict) is None:
            # If not, create a new UserDetails and add it to the list
            init_UserAllDetails_model(user_details_list, results_dict, UserDetails)

        # Add team and schedule data
        equipos = Equipo_Default_Response(extraer_equipos(results_dict, equipos_data))
        horarios = Horario_Default_Response(extraer_horarios(results_dict, horarios_data))

    # Assign the equipos and horarios to each user
    assing_byId(user_details_list,equipos,horarios)
    
    return sorted(user_details_list, key=lambda u: u.id_usuario)
