from databases import Database
import datetime
import discord

aliases = {
    'basculin-blue-striped': 'basculin-bluestriped',
    'basculin-white-striped': 'basculin-whitestriped',
    'charizard-mega-x': 'charizard-megax',
    'charizard-mega-y': 'charizard-megay',
    'chien-pao': 'chienpao',
    'chi-yu': 'chiyu',
    'darmanitan-galar-zen': 'darmanitan-galarzen',
    "farfetch'd": 'farfetchd',
    'gourgeist-small': 'gourgeist',
    'gourgeist-average': 'gourgeist',
    'gourgeist-large': 'gourgeist',
    'gourgeist-super': 'gourgeist',
    'greninja-bond': 'greninja',
    'hakamo-o': 'hakamoo',
    'indeedee-m': 'indeedee',
    'kommo-o': 'kommoo',
    'meowstic-m': 'meowstic',
    'mewtwo-mega-x': 'mewtwo-megax',
    'mewtwo-mega-y': 'mewtwo-megay',
    'necrozma-dawn-wings': 'necrozma-dawnwings',
    'necrozma-dusk-mane': 'necrozma-duskmane',
    'oricorio-baile': 'oricorio',
    "oricorio-pa'u": 'oricorio-pau',
    'porygon-z': 'porygonz',
    'pumpkaboo-small': 'pumpkaboo',
    'pumpkaboo-average': 'pumpkaboo',
    'pumpkaboo-large': 'pumpkaboo',
    'pumpkaboo-super': 'pumpkaboo',
    'rockruff-dusk': 'rockruff',
    'rotom-spin': 'rotom-fan',
    'rotom-freeze': 'rotom-frost',
    'rotom-cut': 'rotom-mow',
    "sirfetch'd": 'sirfetchd',
    'tauros-paldea-combat': 'tauros-paldeacombat',
    'tauros-paldea-blaze': 'tauros-paldeablaze',
    'tauros-paldea-aqua': 'tauros-paldeaaqua',
    'ting-lu': 'tinglu',
    'toxtricity-low-key': 'toxtricity-lowkey',
    'urshifu-rapid-strike': 'urshifu-rapidstrike',
    'wo-chien': 'wochien',
    'zygarde-10%': 'zygarde-10'
}

class Pokemon:
    def __init__(self, p):
        if p['ID'] in ['Mega', 'Primal', 'Ultra']:
            self.name = f"{p['ID']} {p['Name']}"
        else:
            self.name = p['Name']
        self.typing = p['Typing']
        self.abilities = p['Abilities']
        self.h_ability = p['Hidden Ability']
        self.HP = p['HP']
        self.ATK = p['Atk']
        self.DEF = p['Def']
        self.SpA = p['SpA']
        self.SpD = p['SpD']
        self.SPE = p['Spe']
        self.sc = p['Size']
        self.wc = p['Weight']
        self.sig = p['Signature Move or Moves']
        self.traits = p['Traits']
        if p['Sprite Alias'] != '':
            try:
                self.alias = aliases[p['Sprite Alias'].lower()]
            except:
                self.alias = p['Sprite Alias'].lower()
        else:
            try:
                self.alias = aliases[p['Name'].lower()]
            except:
                self.alias = p['Name'].lower()

db = Database('https://docs.google.com/spreadsheets/d/1qIplFdrzRqHl91V7qRBtsb9LuC1TYW--TFoNlTDvpbA/export?format=csv&gid=2042923402')

# convert raw_content (list of dicts) to a dict of Pokemon
for p in db.raw_content:
    if p['ID'] in ['Mega', 'Primal', 'Ultra']:
        db.content[f"{p['ID'].lower()} {p['Name'].lower()}"] = Pokemon(p)
    else:
        db.content[p['Name'].lower()] = Pokemon(p)

def get_pkmn(pokemon: str):
    p = db.get(pokemon)
    embed = discord.Embed(
        color = discord.Color.dark_teal(),
        title = p.name,
        description = p.typing,
        timestamp = datetime.datetime.now()
    )
    embed.set_thumbnail(url = 'https://play.pokemonshowdown.com/sprites/bw/' + p.alias + '.png')
    embed.add_field(name='Abilities', value=p.abilities)
    if p.h_ability != '':
        embed.add_field(name='Hidden Ability', value=p.h_ability)
    embed.add_field(name='Stats', value=f'HP: {p.HP}\nATK: {p.ATK} | DEF: {p.DEF} | SpA: {p.SpA} | SpD: {p.SpD}\nSpeed: {p.SPE}\nSize Class: {p.sc}\nWeight Class: {p.wc}', inline=False)
    if p.sig != '':
        embed.add_field(name='Signature Move', value=p.sig, inline=False)
    if p.traits != '':
        embed.add_field(name='Traits', value=p.traits)

    return embed