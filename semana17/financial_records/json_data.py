import json

#--------------------Gestion de archivos--------------------

class JsonData:
    def __init__(self, path=None):
        self.path = path
        if path == None:
            self.path = 'C:/Users/jovan/Documents/GIT/semana17/financial_records//financial_record.json'
        self.data = []

    def load_file(self):
        with open(self.path) as jsf:
            self.data = json.load(jsf)

    def upload_json(self):
        with open(self.path, 'w') as file:
            json.dump(self.data, file, indent=4)
        self.load_file()