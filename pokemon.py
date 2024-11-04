from databases import Database

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

db = Database('https://docs.google.com/spreadsheets/d/1qIplFdrzRqHl91V7qRBtsb9LuC1TYW--TFoNlTDvpbA/export?format=tsv&gid=2042923402')