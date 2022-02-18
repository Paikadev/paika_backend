from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse
from schemas.interaction import Interaction
from models.interaction import interactions
from config.db import conn
from os import getcwd

interaction = APIRouter()


@interaction.get("/interactions")
def get_interactions():
    return conn.execute(interactions.select()).fetchall()

@interaction.get("/interaction/{id}")
def get_interaction(id: str):
    return conn.execute(interactions.select().where(interactions.c.id == id)).first()

@interaction.post("/interaction")
def create_user(interaction: Interaction):
    new_interaction = {"id": interaction.id,"name": interaction.name, "description": interaction.description,"text": interaction.text,"timer": interaction.timer, "img_url": interaction.img_url}
    result = conn.execute(interactions.insert().values(new_interaction))
    return conn.execute(interactions.select().where(interactions.c.id == result.lastrowid)).first()

@interaction.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    with open(getcwd() + "/"+ file.filename, "wb") as myfile:
        content = await file.read()
        myfile.write(content)
        myfile.close()
    return file.filename

@interaction.get("/file/{name_file}")
def get_file(name_file: str):
    return FileResponse(getcwd() + "/" + name_file)