from databases import Database
import datetime
import discord

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
        self.alias = o.lower()

db = Database('https://docs.google.com/spreadsheets/d/1qIplFdrzRqHl91V7qRBtsb9LuC1TYW--TFoNlTDvpbA/export?format=tsv&gid=2042923402', 1)
for pkmn in db.content:
    mon = db.content[pkmn]
    db.content[pkmn] = Pokemon(mon[1], mon[2], mon[3], mon[4], mon[5], mon[6], mon[7], mon[8], mon[9], mon[10], mon[11], mon[12], mon[13], mon[14], mon[15] if mon[15]!='' else mon[1])

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
        embed.add_field(name='Signature Move', value=p.sig)
    if p.traits != '':
        embed.add_field(name='Traits', value=p.traits)

    return embed