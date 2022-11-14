import ApiScraper
import DbConn

class App:

    def __init__(self):
        self.dbConn = DbConn.DbConn().connection()

    def createTable(self):
        query = """CREATE TABLE IF NOT EXISTS njuskalo_table ( 
                 PRODUCT_ID  CHAR(20) NOT NULL, 
                 LINK TEXT,
                 TITLE TEXT,
                 price_e  VARCHAR(64), 
                 price  VARCHAR(64) 
                 ) """
        self.dbConn.cursor().execute(query)
        return self.dbConn.commit()


print(App().createTable())

    #Call API and save it to self variable

    #Parse data with scraper.py (first refactor it to OOP)