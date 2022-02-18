from fastapi import FastAPI
from routes.user import user
from routes.dolby import dolby
from routes.interaction import interaction
from routes.stream import stream
from fastapi.middleware.cors import CORSMiddleware

import os



app = FastAPI(
    title="Paika API",
    version= "0.1 beta",
    openapi_tags=[
        {
        "name": "Users",
        "description":"Users routes"
    }]
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"message": "Hello World"}



app.include_router(user)
app.include_router(dolby)
app.include_router(interaction)
app.include_router(stream)

