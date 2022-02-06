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
        end = file.index(last, start) + len(second)
        list1 = list(file)
        list1[start:end] = ''
        str1 = ''.join(list1)
        return str1
    except ValueError:
        return ""


start = '<article class="entity-body cf">'
end = '</article>'

i = 0

while i < 11:
    #Create text file for each post

    with open('scraped.txt', 'r') as file:
        data = file.read()

    if( i != 0 ):
        final = find_between(data, start, end)
        file_name = "posts/post_" + str(i) + ".txt"
        file = open(file_name, "w")
        file.write(final + "\n")

    deleted = delete_between(data, start, end)
    file = open("scraped.txt", "w")
    file.write(deleted + "\n")
    i += 1

#add posts to db

j = 1

while j < 11:
    #Create text file for each post

    postname = "posts/post_" + str(j) + ".txt"
    with open(postname, 'r') as files:
        post = files.read()

    final = find_between(data, first, second)
    file_name = "posts/post_" + str(i) + ".txt"
    file = open(file_name, "w")
    file.write(final + "\n")

    deleted = delete_between(data, first, second)
    file = open("scraped.txt", "w")
    file.write(deleted + "\n")
    i += 1