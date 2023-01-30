import pymysql
import json
import requests
import os
import yaml



def find_between(file, first, last):
    try:
        start = file.index(first) + len(first)
        end = file.index(last, start)
        return file[start:end]
    except ValueError:
        return ""


def delete_between(file, first, last):
    try:
        start = file.index(first)
        end = file.index(last, start) + len(last)
        list1 = list(file)
        list1[start:end] = ''
        str1 = ''.join(list1)
        return str1
    except ValueError:
        return ""

def clear_whitespace (input_string):
    string = input_string.split()
    clean_string = "".join(string)
    return clean_string

with open('config.yaml') as f:
    config = yaml.load(stream=f, Loader=yaml.FullLoader)

# DB info from config
db_host = config['db_host']
db_username = config['db_username']
db_password = config['db_password']

# Slack info from config
channel_id = config['channel_id']
webhook_url = config['webhook_url']


start = '<article class="entity-body cf">'
end = '</article>'

id_start = '<a name="'
id_end = '" class='

link_start = 'href="'
title_end = '</a>'

price_start_e = '<strong class="price price--eur">'
price_end_e = '&nbsp;'

price_start = '<strong class="price price--hrk">'
price_end = price_end_e

i = 0

#Connect to DB
connection = pymysql.connect(host=db_host, user=db_username, password=db_password, database='njuskalo')
cur = connection.cursor()

while i < 11:
    #Create text file for each post

    with open('../scraped.txt', 'r') as file:
        post_data = file.read()

    if( i != 0 ):

        #get single post content (skips first because it's advertisement)
        single_post = find_between(post_data, start, end)
        post_id = find_between(single_post, id_start, id_end)

        link_end = post_id + '">'
        title_start = link_end

        # Get usefull info from scraped post
        link = find_between(single_post, link_start, link_end)
        title = find_between(single_post, title_start, title_end)
        price_e = find_between(single_post, price_start_e, price_end_e)
        price = find_between(single_post, price_start, price_end)

        clean_price_e = clear_whitespace(price_e)
        clean_price = clear_whitespace(price)

        cur.execute(
            """SELECT PRODUCT_ID, COUNT(*) FROM njuskalo_table WHERE PRODUCT_ID = %s GROUP BY PRODUCT_ID""",
            (post_id,)
        )
        # gets the number of rows affected by the command executed
        row_count = cur.rowcount

        if row_count == 0 and post_id != "":
            mySql_insert_query = """INSERT INTO njuskalo_table (PRODUCT_ID, LINK, TITLE, price_e, price) 
                                           VALUES (%s, %s, %s, %s, %s) """

            record = (post_id, link, title, clean_price_e, clean_price )
            cur.execute(mySql_insert_query, record)
            connection.commit()

            link_w = "<https://www.njuskalo.hr" + link + str(post_id) + "|" + title + ">"
            total_price = clean_price_e + "€" + " (" + clean_price + "kn)"
            data = {'channel': channel_id, 'text': 'Novi stan!', 'blocks': [
                {'type': 'section',
                 'fields': [{'type': 'mrkdwn', 'text': link_w}, {'type': 'mrkdwn', 'text': total_price} ]},
            ]}

            data_json = json.dumps(data)

            r = requests.post(webhook_url, data=data_json)

    deleted = delete_between(post_data, start, end)
    file = open("../scraped.txt", "w")
    file.write(deleted + "\n")
    i += 1

#close DB connection
cur.close()

os.remove("../scraped.txt")