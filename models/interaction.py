from sqlalchemy import Table, Column
from sqlalchemy.sql.expression import column
from sqlalchemy.sql.sqltypes import VARCHAR, Integer
from config.db import meta, engine

interactions = Table("interactions", meta, Column(
    "id", Integer, primary_key=True), 
    Column("name", VARCHAR(255)),
    Column("description", VARCHAR(255)),
    Column("text", VARCHAR(255)),
    Column("timer", Integer),
    Column("img_url", VARCHAR(255)))

meta.create_all(engine)