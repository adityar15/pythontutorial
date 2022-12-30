import uuid
from .JsonFileHandler import JsonFileHandler


class Book:
    def __init__(self, title="", price=0):
        self.title = title
        self.price = price
        self.id = str(uuid.uuid4())
        self.jsonHandler = JsonFileHandler("books.json")

    def addBook(self, author):
        self.author = author
        book = {
            "title": self.title,
            "price": self.price,
            "author": self.author,
            "id": self.id
        }
        if self.ifBookExists(book):
            print("Book already exists")
            return False

        self.jsonHandler.appendInFile(book)
        # code to save book to file

    def getBook(self, id):
        content = self.getAllBooks()
        
        for index, item in enumerate(content):
            if item["id"] == id:
                return [item, index]
      
        return None

    def updateBook(self, id):
        # code to update book in file
        requiredBook = self.getBook(id)
        book = requiredBook[0]
        index = requiredBook[1]

        if self.title:
            book["title"] = self.title
        if self.price:
            book["price"] = self.price
        
        books = self.getAllBooks()
        books[index] = book
        self.jsonHandler.write({"data":books})

    def deleteBook(self, id):
        # code to delete book from file
        books = self.getAllBooks()
        newBookList = [book for book in books if book["id"] != id]
        self.jsonHandler.write({"data":newBookList})

    def getAllBooks(self):
        # code to get all books from file
        content = self.jsonHandler.read()
        return content["data"]

    def ifBookExists(self, book: dict):
        content = self.jsonHandler.read()
        for item in content["data"]:
            if (item["title"].upper() == book["title"].upper() and 
            item["author"].upper() == book["author"].upper() and item["price"] == book["price"]):
                return True
        return False

    def getBookByIds(self, ids : list):
        books = self.getAllBooks()
        return [book for book in books if book["id"] in ids]

# book = Book("The Alchemist", 600)

# book.addBook("Paulo Coelho")

# book = Book(price=400)
# book.updateBook("a630e7ec-bfbc-4cbc-aa55-93ac19e6f20c")

# print(book.getBook("bb965a6d-e8d2-4b2b-b322-5d3e3779d80d"))