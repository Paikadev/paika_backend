from fastapi import APIRouter
from schemas.interaction import Interaction
from models.interaction import interactions
from config.db import conn

interaction = APIRouter()


@interaction.get("/interactions", response_model=list[Interaction], tags=["Interactions"])
def get_interactions():
    return conn.execute(interactions.select()).fetchall()

@interaction.get("/interaction/{id}", tags=["Intereactions"])
def get_interaction(id: str):
    return conn.execute(interactions.select().where(interactions.c.id == id)).first()

@interaction.post("/interaction", response_model= Interaction, tags=["Interactions"])
def create_user(interaction: Interaction):
    new_interaction = {"id": interaction.id,"name": interaction.name, "description": interaction.description,"text": interaction.text,"timer": interaction.timer, "img_url": interaction.img_url}
    result = conn.execute(interactions.insert().values(new_interaction))
    return conn.execute(interactions.select().where(interactions.c.id == result.lastrowid)).first()