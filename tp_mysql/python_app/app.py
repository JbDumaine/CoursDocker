from sqlalchemy import  create_engine
engine = create_engine("mysql+pymysql://myuser:mypass@database:3306/mydb")
engine.connect()

print(engine)