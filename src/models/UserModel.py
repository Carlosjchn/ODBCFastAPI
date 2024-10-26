from pydantic import BaseModel, Field
from typing import Optional,List
from ..models.HorarioModel import Horario
class User(BaseModel):
    id_usuario: int
    tipo: str
    nombre: str
    email: str
    password: str
    id_equipo: Optional[int] = Field(default=None)
    
def User_Default_Response(results: List[tuple]) -> List[User]:
    return [User(**dict(zip(("id_usuario", "tipo", "nombre", "email", "password", "id_equipo"), row))) for row in results]
    user = []
    for row in results:
        user.append(User(id_usuario=row[0], 
                         tipo=row[1], 
                         nombre=row[2], 
                         email=row[3], 
                         password=row[4], 
                         id_equipo=row[5] if row[5] is not None else None))
    return user

class UserDetails(BaseModel):
    id_usuario: int
    tipo: str
    nombre: str
    email: str
    password: str
    id_equipo: Optional[int] = Field(default=None)
    equipo: Optional[str] = Field(default=None)
    horarios: Optional[List[Horario]] = Field(default=None)
    
    
def User_Details_Response(results: List[tuple]) -> List[UserDetails]:
    return [User(**dict(zip(("id_usuario", "tipo", "nombre", "email", "password", "id_equipo"), row))) for row in results]
