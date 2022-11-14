import os
import psycopg2
from dotenv import dotenv_values

config = dotenv_values()

db_host = os.environ['DB_HOST']
db_user = config['DB_USER']
db_password = config['DB_PASSWORD']
db_port = config["DB_PORT"]
db_name = config["DB_NAME"]

conn = psycopg2.connect(
    host=os.environ['DB_HOST'],
    database=db_name,
    user=db_user,
    password=db_password,
    port=db_port
)

cur = conn.cursor()
query = """CREATE TABLE IF NOT EXISTS njuskalo_table ( 
         PRODUCT_ID  CHAR(20) NOT NULL, 
         LINK TEXT,
         TITLE TEXT,
         price_e  VARCHAR(64), 
         price  VARCHAR(64) 
         ) """

cur.execute(query)
conn.commit()
conn.close()