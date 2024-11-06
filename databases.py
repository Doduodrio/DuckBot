from io import StringIO
import requests
import csv

class Database:
    def __init__(self, url):
        self.url = url
        self.content = {}

        data = requests.get(self.url)
        data.encoding = 'utf-8'
        file = StringIO(data.text)
        self.raw_content = list(csv.DictReader(file))
        
    def get(self, name):
        return self.content[name.lower()]