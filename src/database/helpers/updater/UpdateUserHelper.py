# helper.py

def build_update_query(id_usuario: int, tipo: str = None, nombre: str = None, email: str = None, password: str = None, id_equipo: int = None):
    fields_to_update = {}
    
    if tipo is not None:
        fields_to_update["tipo"] = tipo
    if nombre is not None:
        fields_to_update["nombre"] = nombre
    if email is not None:
        fields_to_update["email"] = email
    if password is not None:
        fields_to_update["password"] = password
    if id_equipo is not None:
        fields_to_update["id_equipo"] = id_equipo
    if not fields_to_update:
        raise ValueError("Debe proporcionar al menos un campo para actualizar.")

    # Adjusted to access the dictionary value correctly
    set_clause = ", ".join([f"{key} = '{fields_to_update[key]}'" for key in fields_to_update.keys()])
    query = f"UPDATE usuario SET {set_clause} WHERE id_usuario = {id_usuario}"
    
    print(query)
    
    return query
