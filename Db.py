import os

import psycopg
from dotenv import dotenv_values

import Logger


class Db:

    def __init__(self):
        config = dotenv_values()
        self.db_host = os.getenv('DB_HOST')
        self.db_user = config['DB_USER']
        self.db_password = config['DB_PASSWORD']
        self.db_port = config["DB_PORT"]
        self.db_name = config["DB_NAME"]

    def connection(self):
        conn = psycopg.connect(
            host=self.db_host,
            dbname=self.db_name,
            user=self.db_user,
            password=self.db_password,
            port=self.db_port
        )
        return conn

    def createTable(self):
        query = """CREATE TABLE IF NOT EXISTS njuskalo_table ( 
                 PRODUCT_ID  CHAR(20) NOT NULL, 
                 LINK TEXT,
                 TITLE TEXT,
                 price_e  VARCHAR(64), 
                 price  VARCHAR(64) 
                 ) """
        try:
            conn = self.connection()
            try:
                conn.cursor().execute(query)
            except Exception as e:
                Logger.logger.error(e)

        except Exception as e:
            Logger.logger.error(e)

        return conn.commit()

    def checkIfExists(self, productId):
        query = """SELECT PRODUCT_ID, COUNT(*) FROM njuskalo_table WHERE PRODUCT_ID = %s GROUP BY PRODUCT_ID""", (productId)
        try:
            conn = self.connection()
            try:
                conn.cursor().execute(query)
            except Exception as e:
                Logger.logger.error(e)

        except Exception as e:
            Logger.logger.error(e)

        return conn
