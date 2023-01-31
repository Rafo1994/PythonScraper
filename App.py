from dotenv import dotenv_values

import ApiScraper
import Db
import Logger
import ProcessData
from SlackNotification import SlackNotification


# Add logger for each process!

class App:

    def __init__(self):
        self.conn = Db.Db().connection()
        config = dotenv_values()
        self.webhookUrl = config['WEBHOOK']
        cur = self.conn.cursor()
        query = """CREATE TABLE IF NOT EXISTS njuskalo_table ( 
                 product_id  CHAR(20) NOT NULL, 
                 link TEXT,
                 title TEXT,
                 price_e  VARCHAR(64), 
                 price  VARCHAR(64) 
                 ) """
        # try and if ok commit
        exec = cur.execute(query)
        # print(exec)
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

            # Change everything accordingly to connection in constructor
            article = processData.getArticleInfo()
            Logger.logger.debug(i)

            cur = self.conn.cursor()
            query = """SELECT product_id, COUNT(*) FROM njuskalo_table WHERE product_id = %s GROUP BY product_id"""
            # try and if ok commit
            exec = cur.execute(query, (article.get("ID"),))
            if exec.rowcount == 0 and article.get("ID") != '':
                query = """INSERT INTO njuskalo_table (product_id, link, title, price_e, price) 
                                               VALUES (%s, %s, %s, %s, %s) """

                sqlParams = (article.get("ID"), article.get("link"), article.get("title"), article.get("price"),
                             article.get("price_kn"))
                cur.execute(query, sqlParams)
                self.conn.commit()

                # send Slack message

                SlackNotification(article.get("ID"), article.get("link"), article.get("title"), article.get("price"),
                                  self.webhookUrl).sendNotification()

            # print(output_data)
            # Check if ID from output data exists in DB -> if YES continue and run deleteBetween method - if NO add it do DB and send a Slack message
            processData.deleteBetween()
            i += 1


App().run()
