from ....models.UserModel import (
    User_Default_Response,
    User_Details_Response,
    User_All_Info_Response,
)


def build_base_query(horarios: bool = False, full_info: bool = False) -> str:
    """Genera la consulta base SELECT para obtener datos de usuario."""
    return "SELECT * FROM usuario u"

def add_joins(details: bool, full_info: bool) -> str:
    """Agrega las cláusulas JOIN según los indicadores."""
    joins = []
    if full_info:
        joins.append("JOIN equipos e ON u.id_equipo = e.id_equipo")
    if details or full_info:
        joins.append("JOIN horarios h ON u.id_usuario = h.id_usuario")
    return " ".join(joins)

def add_filter(userId: int) -> str:
    """Agrega una cláusula WHERE si se proporciona un userId específico."""
    return f" WHERE u.id_usuario={userId}" if userId is not None else ""

def query_builder(userId: int, horarios: bool = False, full_info: bool = False):
    query = (
        f"{build_base_query(horarios, full_info)} "
        f"{add_joins(horarios, full_info)}"
        f"{add_filter(userId)}"
    )
    return query
def get_response_processor(details: bool, full_info: bool):
    """Selecciona el procesador de respuesta adecuado según los indicadores."""
    if full_info:
        return User_All_Info_Response
    elif details:
        return User_Details_Response
    else:
        return User_Default_Response