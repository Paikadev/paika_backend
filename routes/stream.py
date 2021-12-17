from fastapi import APIRouter
from schemas.stream import Stream
from models.stream import streams
from config.db import conn

stream = APIRouter()


@stream.get("/interactions", response_model=list[Stream], tags=["Streams"])
def get_streams():
    return conn.execute(streams.select()).fetchall()

@stream.post("/interaction", response_model= Stream, tags=["Streams"])
def create_stream(stream: Stream):
    new_stream = {"id": stream.id,"id_interaction": stream.id_interaction}
    result = conn.execute(streams.insert().values(new_stream))
    return conn.execute(streams.select().where(streams.c.id == result.lastrowid)).first()