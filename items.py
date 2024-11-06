from databases import Database
import datetime
import discord

class Item:
    def __init__(self, i):
        self.name = i['Item'].strip('-')
        if '\n' in i['Description']:
            self.flavor = i['Description'].split('\n')[0]
            self.description = '\n'.join(i['Description'].split('\n')[1::])
        else:
            self.flavor = i['Description']
            self.description = ''

db = Database('https://docs.google.com/spreadsheets/d/1qIplFdrzRqHl91V7qRBtsb9LuC1TYW--TFoNlTDvpbA/export?format=csv&gid=2023973583')

# convert raw_content (list of dicts) to a dict of Item
for i in range(24, len(db.raw_content)):
    item = db.raw_content[i]
    if item['Item'].startswith('-'):
        db.content[item['Item'].lower().strip('-')] = Item(item)

def get_item(item: str):
    i = db.get(item.lower())
    embed = discord.Embed(
        color = discord.Color.dark_teal(),
        title = i.name,
        description = f'*{i.flavor}*',
        timestamp = datetime.datetime.now()
    )
    embed.add_field(name='Description', value=i.description)

    return embed