from datetime import time, timedelta
from typing import List
from pydantic import BaseModel


class Equipo(BaseModel):
    id_equipo: int
    tipo: str
    nombre: str
    horas_inicio_act : time 
    horas_fin_act: time

def timedelta_to_time(td: timedelta) -> time:
    """Converts a timedelta to a time object."""
    total_seconds = int(td.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return time(hours, minutes, seconds)   
    
def Equipo_Default_Response(results: List[tuple])-> List[Equipo]:
    Equipos = []
    for row in results:
        row_dict = dict(zip(("id_equipo", "tipo", "nombre", "horas_inicio_act", "horas_fin_act"), row))

        if isinstance(row_dict["horas_inicio_act"], timedelta):
            row_dict["horas_inicio_act"] = timedelta_to_time(row_dict["horas_inicio_act"])
        if isinstance(row_dict["horas_fin_act"], timedelta):
            row_dict["horas_fin_act"] = timedelta_to_time(row_dict["horas_fin_act"])

        Equipos.append(Equipo(**row_dict))
        
    return Equipos

    #     equipo = Equipo(
    #         id_equipo=row[0],
    #         tipo=row[1],
    #         nombre=row[2],
    #         horas_inicio_act=timedelta_to_time(row[3]),
    #         hora_fin_act=timedelta_to_time(row[4])
    #     )
    #     Equipos.append(equipo)
    
    # return Equipos