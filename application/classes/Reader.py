from .Person import Person

class Reader(Person):

    def __init__(self, name="", email=""):
        super().__init__(name, email, "reader")
    

    def createReader(self):
        reader = self.getDetails()
        reader["books"] = []
        if self.ifExists("reader"):
            print("Reader already exists")
            return False
        
        self.jsonHandler.appendInFile(reader)
        return True
    

    def getReader(self, id="", email=""):
        return self.getUser("reader", id, email)


    def addBookToCollection(self, bookID):
        readerList = self.getReader(id=self.email)
        reader = readerList[0]
        index = readerList[1]

        if bookID in reader["books"]:
            print("Book already exists in your collection")
            return False
        
        reader["books"].append(bookID)

        readers = self.getAllUsers()

        readers[index] = reader
        self.jsonHandler.write({"data":readers})
    
