import pymysql
import yaml
from dotenv import dotenv_values

config = dotenv_values()

#with open('config.yaml') as f:
    #config = yaml.load(stream=f, Loader=yaml.FullLoader)
# DB info from config
db_host = config['DB_HOST']
db_username = config['DB_USER']
db_password = config['DB_PASSWORD']

# Connect to MariaDB and create database

conn = pymysql.connect(host=db_host, database='njuskalo', user="root", password=db_password, port=3306)

cur = conn.cursor()
cur.execute("""CREATE DATABASE IF NOT EXISTS njuskalo""")
conn.commit()
conn.close()


# Connect to MariaDB and create table

db_conn = pymysql.connect(host=db_host, user=db_username, password=db_password, database='njuskalo')
db_cur = db_conn.cursor()
query = """CREATE TABLE IF NOT EXISTS njuskalo_table ( 
         PRODUCT_ID  CHAR(20) NOT NULL, 
         LINK LONGTEXT,
         TITLE LONGTEXT,
         price_e  VARCHAR(64), 
         price  VARCHAR(64) 
         ) """

db_cur.execute(query)
db_conn.commit()
db_conn.close()