with open("C:/Users/alext/Documents/Programs/Projects/School//Files/books.txt") as book_list:
    for line in book_list:
        book = line.strip()
        print(book)