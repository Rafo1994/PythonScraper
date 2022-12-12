import Db
import Logger
import ApiScraper
import ProcessData

# Add logger for each process!

class App:

    def __init__(self):
        self.conn = Db.Db().connection()
        cur = self.conn.cursor()
        query = """CREATE TABLE IF NOT EXISTS njuskalo_table ( 
                 PRODUCT_ID  CHAR(20) NOT NULL, 
                 LINK TEXT,
                 TITLE TEXT,
                 price_e  VARCHAR(64), 
                 price  VARCHAR(64) 
                 ) """
        # try and if ok commit
        exec = cur.execute(query)
        print(exec)
        self.conn.commit()

    def run(self):
        data = ApiScraper.ApiScraper().sendRequest()
        processData = ProcessData.ProcessData(data)
        i = 0
        while i < 11:
            # Skip first product, because it's ad
            if i == 0:
                processData.deleteBetween()
                i += 1
                continue

            #Change everythin accordingly to connection in constructor
            output_data = processData.getArticleInfo()
            print(type(output_data.get("ID")))
            conn = self.conn.cursor()
            query = """SELECT PRODUCT_ID, COUNT(*) FROM njuskalo_table WHERE PRODUCT_ID = %s GROUP BY PRODUCT_ID"""

            exec = conn.execute(query, (output_data.get("ID"),))
            print(exec.rowCount)
            #print(output_data)
            # Check if ID from output data exists in DB -> if YES continue and run deleteBetween method - if NO add it do DB and send a Slack message
            processData.deleteBetween()
            i += 1
    # Call API and save it to self variable


App().run()

# Parse data with scraper.py (first refactor it to OOP)
