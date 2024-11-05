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
    def __init__(self, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p):
        self.name = a.strip('-')
        self.flavor = b
        self.description = c
        self.type = d
        self.category = e
        self.target = f
        self.BAP = g
        self.acc = h
        self.ENcost = i
        self.effect_chance = j
        self.priority = k
        self.combo_lvl = l
        self.contact = m
        self.snatch = n
        self.reflect = o
        self.tags = p

        if self.name in commands:
            self.move = 'Command'
        elif self.name in z_moves:
            self.move = 'Z-Move'
        elif self.name.startswith('Max ') or self.name.startswith('G-Max '):
            self.move = 'Max Move'
        else:
            self.move = 'Move'

db = Database('https://docs.google.com/spreadsheets/d/1qIplFdrzRqHl91V7qRBtsb9LuC1TYW--TFoNlTDvpbA/export?format=tsv&gid=1023445923', 0)

# convert raw_content (list of tab-separated values) to a dict
for i in range(11, len(db.raw_content)):
    line = db.raw_content[i].split('\t')
    if i%2==0:
        db.content[line[0][1::].lower()] = [line]
    else:
        db.content[line[0][1::].lower()].append(line)

# convert dict[list[list]] to dict[move]
for move in db.content:
    mv = db.content[i]
    db.content[move.lower()] = Move(mv[0][0], mv[1][1].split('\n')[0], mv[1][1].split('\n')[1], mv[0][1], mv[0][2], mv[0][3], mv[0][4], mv[0][5], mv[0][6], mv[0][7], mv[0][8], mv[0][9], mv[0][10], mv[0][11], mv[0][12], mv[0][13])

def get_move(move: str):
    m = db.get(move.lower())
    embed = discord.Embed(
        color = discord.Color.dark_teal(),
        title = m.name,
        value = m.flavor,
        timestamp = datetime.datetime.now()
    )
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
    embed.add_field(name='Additional Info', value=f'Contact: {m.contact}\nSnatch: {m.snatch}\nReflect: {m.reflect}')

    return embed