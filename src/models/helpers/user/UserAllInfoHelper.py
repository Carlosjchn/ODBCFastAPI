from pydantic import BaseModel


def results_allDetails_to_dict(row):
    row_dict = dict(
        zip(
            (
                "id_usuario",
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
                "hora_fin",
            ),
            row,
        )
    )

    return row_dict


def check_existing_user(user_details_list: list, results_dict: dict):
     user = next(
        (u for u in user_details_list if u.id_usuario == results_dict["id_usuario"]),
        None,
    )
     
     return user


def init_UserAllDetails_model(
    user_details_list: list, results_dict: dict, UserDetails: BaseModel
):
    user = UserDetails(
        id_usuario=results_dict["id_usuario"],
        tipo=results_dict["tipo"],
        nombre=results_dict["nombre"],
        email=results_dict["email"],
        password=results_dict["password"],
        id_equipo=results_dict["id_equipo"],
        equipo=[],
        horarios=[],
    )
    user_details_list.append(user)

    return user_details_list


def assing_byId(user_details_list: list, equipos: list, horarios: list):

    for user in user_details_list:
        user.equipo = [equipo for equipo in equipos if equipo.id_equipo == user.id_equipo]
        user.horarios = [h for h in horarios if h.id_usuario == user.id_usuario]

    return user_details_list
