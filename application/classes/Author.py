from .Person import Person

class Author(Person):
    def __init__(self, name="", email=""):
        super().__init__(name, email, "author")  
       
    
    def createAuthor(self):
        author = self.getDetails()
        if self.ifExists("author"):
            print("Author already exists")
            return False
        self.jsonHandler.appendInFile(author)
        return True
  
    
    def getAuthor(self, id="", email=""):
       return self.getUser("author", id, email)

