from typing import Optional, Tuple


def build_delete_query(id_usuario=None, nombre=None):
    if id_usuario is not None and nombre is None:
        return f"DELETE FROM usuario WHERE id_usuario = {id_usuario}"
    if nombre is not None and id_usuario is None:
        return f"DELETE FROM usuario WHERE nombre = {nombre}"
    raise ValueError("Debe proporcionar un ID de usuario o un nombre para eliminar.")