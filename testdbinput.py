import pymysql

item_name = 231
connection = pymysql.connect(host='localhost', user='user1', password='password1', database='njuskalo')
cur = connection.cursor()
mySql_insert_query = """INSERT INTO njuskalo_table (PRODUCT_ID) 
                       VALUES 
                       (231) """

cur.execute(mySql_insert_query)
connection.commit()
print(cur.rowcount, "Record inserted successfully into Laptop table")


cur.execute(
    "SELECT PRODUCT_ID, COUNT(*) FROM njuskalo_table WHERE PRODUCT_ID = %s GROUP BY PRODUCT_ID",
    (item_name,)
)
