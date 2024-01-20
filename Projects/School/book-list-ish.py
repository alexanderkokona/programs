
max_chapters = -1
max_book = ""

# Open file
with open("C:/Users/alext/Documents/Programs/Projects/School/Files/books_and_chapters.txt") as file:


    for line in file:
        parts = line.strip().split(":")
        book = parts[0]
        chapters = int(parts[1])
        scripture = parts[2]

        # print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapters}")

        if chapters > max_chapters:
            max_chapters = chapters 
            max_book = book 

print(f"The book with the most chapters is: {max_book}")
print(f"It has {max_chapters} chapters.")