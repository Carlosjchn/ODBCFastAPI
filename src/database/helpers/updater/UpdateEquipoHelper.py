from datetime import time


def build_update_equipo(id_equipo: int = None, tipo: str = None, nombre: str = None, hora_inicio_act: str = None, hora_fin_act: str = None):
    fields_to_update = {}


    if tipo is not None:
        fields_to_update["tipo"] = tipo
    if nombre is not None:
        fields_to_update["nombre"] = nombre
    if hora_inicio_act is not None:
        fields_to_update["hora_inicio_act"] = hora_inicio_act 
    if hora_fin_act is not None:
        fields_to_update["hora_fin_act"] = hora_fin_act

    # Create the SET clause of the query
    set_clause = ", ".join([f"{key} = '{value}'" for key, value in fields_to_update.items()])

    # Build the final query string
    query = f"UPDATE equipos SET {set_clause} WHERE id_equipo = {id_equipo};"
    
    return query
