from fastapi import APIRouter, Response, status
from starlette.responses import Response
from config.db import conn
from models.user import users
from schemas.user import User
from starlette.status import HTTP_204_NO_CONTENT


user = APIRouter()

@user.get("/users")
def get_users():
    return conn.execute(users.select()).fetchall()

@user.post("/users")
def create_user(user: User):
    new_user = {"id": user.id,"name": user.name, "username": user.username,"phone": user.phone, "avatar_url": user.avatar_url}
    result = conn.execute(users.insert().values(new_user))
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()

@user.get("/users/{id}")
def get_user(id: str):
    return conn.execute(users.select().where(users.c.id == id)).first()

@user.delete("/users/{id}", status_code= status.HTTP_204_NO_CONTENT)
def delete_user(id: str):
    conn.execute(users.delete().where(users.c.id == id))
    return Response(status_code= HTTP_204_NO_CONTENT)

@user.get("/users/login/")
def login(phone: str):
    return conn.execute(users.select().where(users.c.phone == phone)).first()
