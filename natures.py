from io import StringIO
import datetime
import discord
import requests

class Nature:
    def __init__(self, n):
        self.name = n[0]
        self.effect = n[1]

# no using Database here because the NATURES sheet is formatted differently
data = requests.get('https://docs.google.com/spreadsheets/d/1qIplFdrzRqHl91V7qRBtsb9LuC1TYW--TFoNlTDvpbA/export?format=tsv&gid=54976138')
data.encoding = 'utf-8'
file = StringIO(data.text)
db_raw = file.readlines()
db = {}

# convert raw_content (list of dicts) to a dict of Nature
for i in range(2, len(db_raw)):
    line = db_raw[i].split('\t')
    db[line[0].lower()] = Nature(line)

def get_nature(nature: str):
    n = db[nature.lower()]
    embed = discord.Embed(
        color = discord.Color.dark_teal(),
        title = n.name,
        description = n.effect,
        timestamp = datetime.datetime.now()
    )

    return embed