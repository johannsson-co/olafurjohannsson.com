import json

class AppSettings:
    def __init__(self, fileName='app.config'):
        
        with open(fileName) as f:
            self.data = json.load(f)
    
    def get(self, key):
        return self.data[key]   