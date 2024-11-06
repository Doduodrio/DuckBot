from databases import Database
import datetime
import discord

class Ability:
    def __init__(self, a):
        self.name = a['Ability'].strip('-')
        if '\n' in a['Description']:
            self.flavor = a['Description'].split('\n')[0]
            self.description = '\n'.join(a['Description'].split('\n')[1::])
        else:
            self.flavor = a['Description']
            self.description = ''

db = Database('https://docs.google.com/spreadsheets/d/1qIplFdrzRqHl91V7qRBtsb9LuC1TYW--TFoNlTDvpbA/export?format=csv&gid=1445814381')

# convert raw_content (list of dicts) to a dict of Ability
for i in range(10, len(db.raw_content)):
    a = db.raw_content[i]
    db.content[a['Ability'].lower().strip('-')] = Ability(a)

def get_ability(ability: str):
    a = db.get(ability.lower())
    embed = discord.Embed(
        color = discord.Color.dark_teal(),
        title = a.name,
        description = f'*{a.flavor}*',
        timestamp = datetime.datetime.now()
    )
    if len(a.description) > 1024:
        embed.add_field(name='Description', value='The description is too long to fit.')
    elif a.description != '':
        embed.add_field(name='Description', value=a.description)
    
    return embed