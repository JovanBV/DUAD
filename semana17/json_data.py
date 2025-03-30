import json

class JsonData:
    def __init__(self, path="semana17/financial_record.json"):
        self.path = path
        self.data = []

    def load_file(self):
        with open(self.path) as jsf:
            self.data = json.load(jsf)

    def upload_json(self):
        with open(self.path, 'w') as file:
            json.dump(self.data, file, indent=4)
        self.load_file()