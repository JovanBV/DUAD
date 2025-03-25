import json

class jsonData():
    def __init__(self, path='C:/Users/jovan/Documents/GIT/semana17/financial_record.json'):
        self.path = path
        self.data = ''
        self.load_file()

    def load_file(self):
        with open(self.path) as jsf:
            self.data = json.load(jsf)

    def upload_json(self):
        with open(self.path, 'w') as file:
            json.dump(self.data, file, indent=4)
        self.load_file()

