
def extraer_equipos(row_dict, equipos_data):
    # Solo agregar si el equipo no está ya en equipos_data
    if row_dict["id_equipo"] is not None:
        # Verifica si el id_equipo ya está en equipos_data
        if not any(equipo[0] == row_dict["id_equipo_e"] for equipo in equipos_data):
            equipos_data.append(
                (
                    row_dict["id_equipo_e"],
                    row_dict["tipo_e"],
                    row_dict["nombre_e"],
                    row_dict["horas_inicio_act"],
                    row_dict["horas_fin_act"],
                )
            )

    # Convertir los horarios a objetos Horario usando el método Horario_Default_Response
    return equipos_data


def extraer_horarios(row_dict, horarios_data):
    # Agregar el horario correspondiente a la lista
    if row_dict["id_horario"] is not None:
        horarios_data.append(
            (
                row_dict["id_usuario_h"],
                row_dict["id_horario"],
                row_dict["fecha"],
                row_dict["hora_inicio"],
                row_dict["hora_fin"],
            )
        )

    # Convertir los horarios a objetos Horario usando el método Horario_Default_Response
    return horarios_data
