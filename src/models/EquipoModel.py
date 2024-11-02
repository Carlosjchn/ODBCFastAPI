from datetime import time, timedelta
from typing import List
from pydantic import BaseModel
from .helpers.horario.HorarioModelHelper import timedelta_to_time


###############
# MODELO BASE #
###############


class Equipo(BaseModel):
    id_equipo: int
    tipo: str
    nombre: str
    horas_inicio_act: time
    horas_fin_act: time


def Equipo_Default_Response(results: List[tuple]) -> List[Equipo]:
    Equipos = []
    for row in results:
        row_dict = dict(
            zip(
                ("id_equipo", "tipo", "nombre", "horas_inicio_act", "horas_fin_act"),
                row,
            )
        )

        if isinstance(row_dict["horas_inicio_act"], timedelta):
            row_dict["horas_inicio_act"] = timedelta_to_time(
                row_dict["horas_inicio_act"]
            )
        if isinstance(row_dict["horas_fin_act"], timedelta):
            row_dict["horas_fin_act"] = timedelta_to_time(row_dict["horas_fin_act"])

        Equipos.append(Equipo(**row_dict))

    return Equipos
