from databases import Database
import datetime
import discord

commands = [
    'Aim',
    'Chill',
    'Cover',
    'Forme Shift',
    'Hide',
    'Struggle',
    'Ball Reject'
]
z_moves = [
    'Savage Spin-Out',
    'Black Hole Eclipse',
    'Devastating Drake',
    'Gigavolt Havoc',
    'Twinkle Tackle',
    'All-Out Pummeling',
    'Inferno Overdrive',
    'Supersonic Skystrike',
    'Never-Ending Nightmare',
    'Bloom Doom',
    'Tectonic Rage',
    'Subzero Slammer',
    'Breakneck Blitz',
    'Acid Downpour',
    'Shattered Psyche',
    'Continental Crush',
    'Corkscrew Crash',
    'Hydro Vortex',
    'Catastropika',
    '10,000,000 Volt Thunderbolt',
    'Stoked Sparksurfer',
    'Extreme Evoboost',
    'Pulverizing Pancake',
    'Genesis Supernova',
    'Sinister Arrow Raid',
    'Malicious Moonsault',
    'Oceanic Operetta',
    'Splintered Stormshards',
    "Let's Snuggle Forever",
    'Clangorous Soulblaze',
    'Guardian of Alola',
    'Searing Sunraze Smash',
    'Menacing Moonraze Maelstrom',
    'Light That Burns the Sky',
    'Soul-Stealing 7-Star Strike'
]

class Move:
    def __init__(self, m, n):
        self.name = m['● '].strip('-')
        if '\n' in n['Type']:
            self.flavor = n['Type'].split('\n')[0]
            self.description = '\n'.join(n['Type'].split('\n')[1::])
        else:
            self.flavor = n['Type']
            self.description = ''
        self.type = m['Type']
        self.category = m['Category']
        self.target = m['Target']
        self.BAP = m['BAP']
        self.acc = m['Acc']
        self.ENcost = m['En Cost']
        self.effect_chance = m['Effect%']
        self.priority = m['Priority']
        self.combo_lvl = m['Combo Lv.']
        self.contact = m['Contact?']
        self.snatch = m['Snatch?']
        self.reflect = m['Reflect?']
        self.tags = m['Tags']

        if self.name in commands:
            self.move = 'Command'
        elif self.name in z_moves:
            self.move = 'Z-Move'
        elif self.name.startswith('Max ') or self.name.startswith('G-Max '):
            self.move = 'Max Move'
        else:
            self.move = 'Move'

db = Database('https://docs.google.com/spreadsheets/d/1qIplFdrzRqHl91V7qRBtsb9LuC1TYW--TFoNlTDvpbA/export?format=csv&gid=1023445923')

# convert raw_content (list of dicts) to a dict of Move
for i in range(0, len(db.raw_content), 2):
    row1 = db.raw_content[i]
    row2 = db.raw_content[i+1]
    db.content[row1['● '].lower().strip('-')] = Move(row1, row2)

def get_move(move: str):
    m = db.get(move.lower())
    embed = discord.Embed(
        color = discord.Color.dark_teal(),
        title = f'{m.name} ({m.move})',
        description = f'*{m.flavor}*',
        timestamp = datetime.datetime.now()
    )
    if m.description != '':
        embed.add_field(name='Description', value=m.description, inline=False)
    embed.add_field(name='Category', value=m.category)
    embed.add_field(name='Type', value=m.type)
    embed.add_field(name='Accuracy', value=m.acc)
    embed.add_field(name='BAP', value=m.BAP)
    embed.add_field(name='Energy Cost', value=m.ENcost)
    embed.add_field(name='Target', value=m.target)
    embed.add_field(name='Effect Chance', value=m.effect_chance)
    embed.add_field(name='Priority', value=m.priority)
    embed.add_field(name='Tags', value=m.tags)
    embed.add_field(name='Contact', value=m.contact)
    embed.add_field(name='Snatch', value=m.snatch)
    embed.add_field(name='Reflect', value=m.reflect)

    return embed