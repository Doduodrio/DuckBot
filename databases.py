from io import StringIO
import requests

class Database:
    def __init__(self, url, key):
        self.url = url
        self.content = {}

        data = requests.get(self.url)
        data.encoding = 'utf-8'
        file = StringIO(data.text)
        self.raw_content = file.readlines()
        
    def get(self, name):
        return self.content[name.lower()]