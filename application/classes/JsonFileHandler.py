import os

# w - write
# r - read
# a - append
# x - create

import json

class JsonFileHandler:

    def __init__(self, file_name):
        realpath = os.path.realpath(__file__)
        directory = os.path.dirname(realpath)
        self.filePath = os.path.join(directory, f"../storage/{file_name}")

    def appendInFile(self, data:dict):
        content = self.read()
        content["data"].append(data)
        self.write(content)
        return True

    def write(self, data : dict):
        content = json.dumps(data)
        with open(self.filePath, "w") as file:
            file.write(content)
        return True
    
    def read(self):
        content = {"data": []}
        with open(self.filePath, "r") as file:
            stringContent = file.read()
            if not stringContent == "":
                content = json.loads(stringContent)
        
        return content