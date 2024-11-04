import requests

from io import StringIO

class Pokemon:
    def __init__(self, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o):
        self.name = a
        self.typing = b
        self.abilities = c
        self.h_ability = d
        self.HP = e
        self.ATK = f
        self.DEF = g
        self.SpA = h
        self.SpD = i
        self.SPE = j
        self.sc = k
        self.wc = l
        self.sig = m
        self.traits = n
        self.alias = o
    
    def __str__(self):
        return f'''{self.name}
Typing: {self.typing}, Abilities: {self.abilities}, Hidden Ability: {self.h_ability}
HP: {self.HP}
ATK: {self.ATK} | DEF: {self.DEF} | SpA: {self.SpA} | SpD: {self.SpD}
Speed: {self.SPE}
Size Class: {self.sc}
Weight Class: {self.wc}
Signature Move: {self.sig}
Traits: {self.traits}
Sprite Alias: {self.alias}'''

class Database:
    def __init__(self, url):
        self.url = url
        self.content = {}
        data = requests.get(self.url)
        data.encoding = 'utf-8'
        file = StringIO(data.text)
        file_list = file.readlines()
        for i in file_list:
            if (i.startswith('152')):
                break
            line = i.split('\t')
            self.content[line[1].lower()] = Pokemon(line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[12], line[13], line[14])
        
    def get_pkmn(self, name):
        return self.content[name.lower()]

db_pokemon = Database('https://docs.google.com/spreadsheets/d/1qIplFdrzRqHl91V7qRBtsb9LuC1TYW--TFoNlTDvpbA/export?format=tsv&gid=2042923402')
doduo = db_pokemon.get_pkmn('doduO')
print(doduo)