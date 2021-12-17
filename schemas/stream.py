from pydantic import BaseModel

class Stream(BaseModel):
    id: int
    id_interaction: int