import uuid
from .JsonFileHandler import JsonFileHandler

class Person:
    def __init__(self, name="", email="", role=""):
        self.name = name
        self.email = email
        self.role = role
        self.id = str(uuid.uuid4())
        self.jsonHandler = JsonFileHandler("user.json")
    
    def getDetails(self):
        return {
            "name": self.name,
            "email": self.email,
            "role": self.role,
            "id": self.id
        }
    
    def ifExists(self, role):
        content = self.getAllUsers()
        for item in content:
            if item["email"] == self.email and item["role"] == role:
                return True
        return False
    
    def getAllUsers(self):
        content = self.jsonHandler.read()
        return content["data"]

    def getUser(self, role, id="", email=""):
        content = self.getAllUsers()
        for index, person in enumerate(content):
            if (person["id"] == id or person["email"] == email) and person["role"] == role:
                return [person, index]
        return None
