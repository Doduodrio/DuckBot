from databases import Database
import datetime
import discord

aliases = {
    'basculin-blue-striped': 'basculin-bluestriped',
    'basculin-white-striped': 'basculin-whitestriped',
    'charizard-mega-x': 'charizard-megax',
    'charizard-mega-y': 'charizard-megay',
    'darmanitan-galar-zen': 'darmanitan-galar',
    'gourgeist-small': 'gourgeist',
    'gourgeist-average': 'gourgeist',
    'gourgeist-large': 'gourgeist',
    'gourgeist-super': 'gourgeist',
    'greninja-bond': 'greninja',
    'indeedee-m': 'indeedee',
    'meowstic-m': 'meowstic',
    'mewtwo-mega-x': 'mewtwo-megax',
    'mewtwo-mega-y': 'mewtwo-megay',
    'necrozma-dawn-wings': 'necrozma-dawnwings',
    'necrozma-dusk-mane': 'necrozma-duskmane',
    'oricorio-baile': 'oricorio',
    "oricorio-pa'u": 'oricorio-pau',
    'pumpkaboo-small': 'pumpkaboo',
    'pumpkaboo-average': 'pumpkaboo',
    'pumpkaboo-large': 'pumpkaboo',
    'pumpkaboo-super': 'pumpkaboo',
    'rockruff-dusk': 'rockruff',
    'rotom-spin': 'rotom-fan',
    'rotom-freeze': 'rotom-frost',
    'rotom-cut': 'rotom-mow',
    'tauros-paldea-combat': 'tauros-paldeacombat',
    'tauros-paldea-blaze': 'tauros-paldeablaze',
    'tauros-paldea-aqua': 'tauros-paldeaaqua',
    'toxtricity-low-key': 'toxtricity-lowkey',
    'urshifu-rapid-strike': 'urshifu-rapidstrike',
    'zygarde-10%': 'zygarde-10'
}

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
        try:
            self.sprite = aliases[a.lower()]
        except:
            self.sprite = a.lower()

db = Database('https://docs.google.com/spreadsheets/d/1qIplFdrzRqHl91V7qRBtsb9LuC1TYW--TFoNlTDvpbA/export?format=tsv&gid=2042923402', 1)
for pkmn in db.content:
    mon = db.content[pkmn]
    if mon[0] in ['Mega', 'Primal', 'Ultra']:
        name = f'{mon[0]} {mon[1]}'
    else:
        name = mon[1]
    db.content[pkmn] = Pokemon(name, mon[2], mon[3], mon[4], mon[5], mon[6], mon[7], mon[8], mon[9], mon[10], mon[11], mon[12], mon[13], mon[14], mon[15])

def get_pkmn(pokemon: str):
    p = db.get(pokemon)
    embed = discord.Embed(
        color = discord.Color.dark_teal(),
        title = p.name,
        description = p.typing,
        timestamp = datetime.datetime.now()
    )
    embed.set_thumbnail(url = 'https://play.pokemonshowdown.com/sprites/bw/' + p.sprite + '.png')
    embed.add_field(name='Abilities', value=p.abilities)
    if p.h_ability != '':
        embed.add_field(name='Hidden Ability', value=p.h_ability)
    embed.add_field(name='Stats', value=f'HP: {p.HP}\nATK: {p.ATK} | DEF: {p.DEF} | SpA: {p.SpA} | SpD: {p.SpD}\nSpeed: {p.SPE}\nSize Class: {p.sc}\nWeight Class: {p.wc}', inline=False)
    if p.sig != '':
        embed.add_field(name='Signature Move', value=p.sig)
    if p.traits != '':
        embed.add_field(name='Traits', value=p.traits)

    return embed