from databases import Database
import datetime
import discord

class Nature:
    def __init__(self, n):
        self.name = n['Nature']
        self.effect = n['Modifiers']

db = Database('https://docs.google.com/spreadsheets/d/1qIplFdrzRqHl91V7qRBtsb9LuC1TYW--TFoNlTDvpbA/export?format=csv&gid=54976138')

# convert raw_content (list of dicts) to a dict of Nature
for i in range(2, len(db.raw_content)):
    n = db.raw_content[i]
    db.content[n['Nature'].lower()] = Nature(n)

def get_nature(nature: str):
    n = db.get(nature.lower())
    embed = discord.Embed(
        color = discord.Color.dark_teal(),
        title = n.name,
        description = n.effect,
        timestamp = datetime.datetime.now()
    )

    return embed