import pymysql

#Connect to MariaDB and create database

conn = pymysql.connect(host='localhost', user='user1', password='password1')
cur = conn.cursor()
cur.execute("""CREATE DATABASE IF NOT EXISTS njuskalo""")
conn.commit()
conn.close()


#Connect to MariaDB and create table

db_conn = pymysql.connect(host='localhost', user='user1', password='password1', database='njuskalo')
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