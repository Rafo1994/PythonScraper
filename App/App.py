#import Db
import Logger
import ApiScraper
import ProcessData


class App:

    #def __init__(self):
        #db = Db.Db()
        #db.createTable()
        #self.dbConn = db.connection()

    def run(self):
        data = ApiScraper.ApiScraper().sendRequest()
        processData = ProcessData.ProcessData(data)
        i = 0
        output = ""
        while i < 11:
            if i == 0:
                processData.deleteBetween()
                i += 1
                continue
            #print("Before deleting: " + processData.article)
            output_data = processData.getArticleInfo()
            print(output_data)
            processData.deleteBetween()
            #print("After deleting: " + processData.article)
            i += 1
        return output
    # Call API and save it to self variable


App().run()

# Parse data with scraper.py (first refactor it to OOP)
