from pydantic import BaseModel, Field
from typing import Optional,List

class User(BaseModel):
    id_usuario: int
    tipo: str
    nombre: str
    email: str
    password: str
    id_equipo: Optional[int] = Field(default=None)
    
def User_Default_Response(results: List[tuple]) -> List[User]:
    user = []
    for row in results:
        user.append(User(id_usuario=row[0], 
                         tipo=row[1], 
                         nombre=row[2], 
                         email=row[3], 
                         password=row[4], 
                         id_equipo=row[5] if row[5] is not None else None))
    return user