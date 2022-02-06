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

while i < 11:
    #Create text file for each post

    with open('scraped.txt', 'r') as file:
        data = file.read()

    if( i != 0 ):

        #get single post content (skips first because it's advertisement)
        single_post = find_between(data, start, end)
        post_id = find_between(single_post, id_start, id_end)
        link_end = post_id + '">'
        title_start = link_end

        link = find_between(single_post, link_start, link_end)
        title = find_between(single_post, title_start, title_end)
        price_e = find_between(single_post, price_start_e, price_end_e)
        price = find_between(single_post, price_start, price_end)

        clean_price_e = clear_whitespace(price_e)
        clean_price = clear_whitespace(price)


        file_name = "posts_clean/post_" + str(i) + "_data.txt"
        file = open(file_name, "w")
        file.write(post_id + "\n" + link + post_id + "\n" + title  + "\n" + clean_price_e  + "\n" + clean_price)

    deleted = delete_between(data, start, end)
    file = open("scraped.txt", "w")
    file.write(deleted + "\n")
    i += 1