from sqlalchemy import Table, Column
from sqlalchemy.sql.expression import column
from sqlalchemy.sql.sqltypes import VARCHAR, Integer
from config.db import meta, engine

streams = Table("streams", meta, Column(
    "stream_key", Integer, primary_key=True), 
    Column("id_interaction", VARCHAR(255)),)

meta.create_all(engine)