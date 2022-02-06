def find_between(file, first, last):
    try:
        start = file.index(first) + len(first)
        end = file.index(last, start)
        return file[start:end]
    except ValueError:
        return ""



i = 1

while i < 11:
    #Create text file for each post

    with open('scraped.txt', 'r') as file:
        data = file.read()

    if( i != 0 ):
        final = find_between(data, first, second)
        file_name = "posts/post_" + str(i) + ".txt"
        file = open(file_name, "w")
        file.write(final + "\n")

    deleted = delete_between(data, first, second)
    file = open("scraped.txt", "w")
    file.write(deleted + "\n")
    i += 1
