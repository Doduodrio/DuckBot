from databases import Database
import datetime
import discord

class Condition:
    def __init__(self, c):
        self.name = c['Condition'].strip('-')
        if '\n' in c['Description']:
            self.flavor = c['Description'].split('\n')[0]
            self.description = '\n'.join(c['Description'].split('\n')[1::])
        else:
            self.flavor = c['Description']
            self.description = ''
        self.default_duration = c['Default Duration']

db = Database('https://docs.google.com/spreadsheets/d/1qIplFdrzRqHl91V7qRBtsb9LuC1TYW--TFoNlTDvpbA/export?format=csv&gid=1137568958')

# convert raw_content (list of dicts) to a dict of Condition
for c in db.raw_content:
    if c['Condition'].startswith('-'):
        db.content[c['Condition'].lower().strip('-')] = Condition(c)

def get_condition(condition: str):
    c = db.get(condition.lower())
    embed = discord.Embed(
        color = discord.Color.dark_teal(),
        title = c.name,
        description = f'*{c.flavor}*',
        timestamp = datetime.datetime.now()
    )
    embed.add_field(name='Description', value=c.description, inline=False)
    if c.default_duration != '':
        embed.add_field(name='Default Duration', value=c.default_duration)
    
    return embed