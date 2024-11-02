
from pydantic import BaseModel


def resultsDetail_to_dict(row):
    row_dict = dict(
        zip(
            (
                "id_usuario",
                "tipo",
                "nombre",
                "email",
                "password",
                "id_equipo",
                "id_usuario_h",
                "id_horario",
                "fecha",
                "hora_inicio",
                "hora_fin",
            ),
            row,
        )
    )

    return row_dict


def initUserDetailsModel(resultsquery_dict: dict, user_details_list: list, UserBasicDetails: BaseModel):
    if not any(
        user.id_usuario == resultsquery_dict["id_usuario"] for user in user_details_list
    ):
        user_details_list.append(
            UserBasicDetails(
                id_usuario=resultsquery_dict["id_usuario"],
                tipo=resultsquery_dict["tipo"],
                nombre=resultsquery_dict["nombre"],
                email=resultsquery_dict["email"],
                password=resultsquery_dict["password"],
                id_equipo=resultsquery_dict["id_equipo"],
                horarios=[],  # Inicializar como lista vacía
            )
        )

    return user_details_list

def asignarHorarios(user_details_list: list, horarios: list):
    for user in user_details_list:
        user.horarios = [h for h in horarios if h.id_usuario == user.id_usuario]
        
    return user_details_list