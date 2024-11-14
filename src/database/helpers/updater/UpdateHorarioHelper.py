def build_update_horario(id_horario: int = None, id_usuario: int = None, fecha: str = None, hora_inicio: str = None, hora_fin: str = None):
    fields_to_update = {}

    if fecha is not None:
        fields_to_update["fecha"] = fecha
    if hora_inicio is not None:
        fields_to_update["hora_inicio"] = hora_inicio
    if hora_fin is not None:
        fields_to_update["hora_fin"] = hora_fin

    set_clause = ", ".join([f"{key} = '{value}'" for key, value in fields_to_update.items()])

    where_clause = f"id_horario = {id_horario}"
    if id_usuario is not None:
        where_clause += f" OR id_usuario = {id_usuario}"


    query = f"UPDATE horarios SET {set_clause} WHERE {where_clause}"
    
    print (query)
    
    return query
