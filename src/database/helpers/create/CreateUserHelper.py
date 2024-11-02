def validar_user_data(
    tipo: str, nombre: str, email: str, password: str, id_equipo: int
):

    user_data = [tipo, nombre, email, password, id_equipo]

    # Validaciones simples (puedes agregar más según sea necesario)
    if not user_data[1]:
        return {"error": "El nombre es requerido."}
    if not user_data[2]:
        return {"error": "El correo electrónico es requerido."}
    if not user_data[3]:
        return {"error": "La contraseña es requerida."}

    return user_data
