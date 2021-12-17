from sqlalchemy import Table, Column
from sqlalchemy.sql.expression import column
from sqlalchemy.sql.sqltypes import VARCHAR, Integer
from config.db import meta, engine

users = Table("users", meta, Column(
    "id", Integer, primary_key=True), 
    Column("name", VARCHAR(255)),
    Column("username", VARCHAR(255)),
    Column("phone", VARCHAR(255)),
    Column("avatar_url", VARCHAR(255)))

meta.create_all(engine)