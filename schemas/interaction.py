from pydantic import BaseModel
from sqlalchemy.sql.expression import text

class Interaction(BaseModel):
    id: int
    name: str
    description: str
    text: str
    timer: int
    img_url: str