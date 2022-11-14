import os
import psycopg2
from dotenv import dotenv_values

class DbConn:

    def __init__(self):
        config = dotenv_values()
        self.db_host = os.environ['DB_HOST']
        self.db_user = config['DB_USER']
        self.db_password = config['DB_PASSWORD']
        self.db_port = config["DB_PORT"]
        self.db_name = config["DB_NAME"]

    def connection(self):
        self.conn = psycopg2.connect(
            host=self.db_host,
            database=self.db_name,
            user=self.db_user,
            password=self.db_password,
            port=self.db_port
        )
        return self.conn

    def cursor(self):
        return self.dbConn().cursor()