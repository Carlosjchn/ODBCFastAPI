from pydantic import BaseModel, Field
from typing import Optional,List
from datetime import date, time, timedelta

class Horario(BaseModel):
    id_horario: int
    id_usuario: int
    fecha : date 
    hora_inicio : time
    hora_fin : time


def timedelta_to_time(td: timedelta) -> time:
    """Converts a timedelta to a time object."""
    total_seconds = int(td.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return time(hours, minutes, seconds)
    
def Horario_Default_Response(results: List[tuple]) -> List[Horario]:
    horarios = []
    for row in results:
        row_dict = dict(zip(("id_horario", "id_usuario", "fecha", "hora_inicio", "hora_fin"), row))
        
        # Convert timedelta to time if needed
        if isinstance(row_dict["hora_inicio"], timedelta):
            row_dict["hora_inicio"] = timedelta_to_time(row_dict["hora_inicio"])
        if isinstance(row_dict["hora_fin"], timedelta):
            row_dict["hora_fin"] = timedelta_to_time(row_dict["hora_fin"])
        
        horarios.append(Horario(**row_dict))
    return horarios
    # return [Horario(**dict(zip(("id_horario", "id_usuario", "fecha", "hora_inicio", "hora_fin"), row))) for row in results]

