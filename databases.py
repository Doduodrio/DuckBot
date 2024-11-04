from io import StringIO
import requests

class Database:
    def __init__(self, url, key):
        self.url = url
        self.content = {}
        data = requests.get(self.url)
        data.encoding = 'utf-8'
        file = StringIO(data.text)
        file_list = file.readlines()
        for i in file_list:
            line = i.split('\t')
            self.content[line[key].lower().strip('-')] = line
        
    def get(self, name):
        return self.content[name.lower()]