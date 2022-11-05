import json

f = open("final_books_dataset.json")

y = json.load(f)
bookTitles = []
print("Number of books: " + str(len(y)))
for book in y:
    if book['title'] in bookTitles:
        print("Repeated book!: " + book['title'])
    else:
        bookTitles.append(book['title'])
