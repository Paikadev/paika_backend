from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://admin:paikateam@paika.cv2xaalgsmwz.us-east-2.rds.amazonaws.com:3306/paika")

meta = MetaData()

conn = engine.connect()