import datetime
import discord

TYPE_CHART = [
    [0, 0, 0, 0, 0, 1, 2, 2, 0, 1, 1, 0, 0, 0, 0, 2, 0, 0], # bug
    [2, 1, 0, 0, 2, 2, 0, 0, 1, 0, 0, 0, 0, 0, 3, 0, 0, 0], # dark
    [0, 0, 2, 1, 2, 0, 1, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 1], # dragon
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0], # electric
    [1, 1, 3, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0], # fairy
    [1, 1, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0], # fighting
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 2, 1, 0, 0, 0, 2, 1, 2], # fire
    [1, 0, 0, 2, 0, 1, 0, 0, 0, 1, 3, 2, 0, 0, 0, 2, 0, 0], # flying
    [1, 2, 0, 0, 0, 3, 0, 0, 2, 0, 0, 0, 3, 1, 0, 0, 0, 0], # ghost
    [2, 0, 0, 1, 0, 0, 2, 2, 0, 1, 1, 2, 0, 2, 0, 0, 0, 1], # grass
    [0, 0, 0, 3, 0, 0, 0, 0, 0, 2, 0, 2, 0, 1, 0, 1, 0, 2], # ground
    [0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 1, 0, 0, 0, 2, 2, 0], # ice
    [0, 0, 0, 0, 0, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0], # normal
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 2, 0, 0, 1, 2, 0, 0, 0], # poison
    [2, 2, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0], # psychic
    [0, 0, 0, 0, 0, 2, 1, 1, 0, 2, 2, 0, 1, 1, 0, 0, 2, 2], # rock
    [1, 0, 1, 0, 1, 2, 2, 1, 0, 1, 2, 1, 1, 3, 1, 1, 1, 0], # steel
    [0, 0, 0, 2, 0, 0, 1, 0, 0, 2, 0, 1, 0, 0, 0, 0, 1, 1] # water
]
TYPES = ['bug', 'dark', 'dragon', 'electric', 'fairy', 'fighting', 'fire', 'flying', 'ghost', 'grass', 'ground', 'ice', 'normal', 'poison', 'psychic', 'rock', 'steel', 'water']

def matchup(type1, type2):
    # type matchup of type1 used on type2
    return TYPE_CHART[TYPES.index(type2)][TYPES.index(type1)]

def offensive_matchup(types):
    # offensive type matchups of type1
    output = {'bug': 0, 'dark': 0, 'dragon': 0, 'electric': 0, 'fairy': 0, 'fighting': 0, 'fire': 0, 'flying': 0, 'ghost': 0, 'grass': 0, 'ground': 0, 'ice': 0, 'normal': 0, 'poison': 0, 'psychic': 0, 'rock': 0, 'steel': 0, 'water': 0}
    for type2 in TYPES:
        for type1 in types:
            m = matchup(type1, type2)
            try:
                if m == 1:
                    output[type2] -= 1
                elif m == 2:
                    output[type2] += 1
                elif m == 3:
                    output[type2] = None
            except:
                break
    return output

def defensive_matchup(types):
    # defensive type matchups of type2
    output = {'bug': 0, 'dark': 0, 'dragon': 0, 'electric': 0, 'fairy': 0, 'fighting': 0, 'fire': 0, 'flying': 0, 'ghost': 0, 'grass': 0, 'ground': 0, 'ice': 0, 'normal': 0, 'poison': 0, 'psychic': 0, 'rock': 0, 'steel': 0, 'water': 0}
    for type1 in TYPES:
        for type2 in types:
            m = matchup(type1, type2)
            try:
                if m == 1:
                    output[type2] -= 1
                elif m == 2:
                    output[type2] += 1
                elif m == 3:
                    output[type2] = None
            except:
                break
    return output

def get_offensive_matchup(types):
    a = offensive_matchup(types)

    offensive = {'Super Effective':  [], 'Not Very Effective': [], 'Ineffective': []}
    for t in TYPES:
        type_ = t.capitalize()
        if a[t] is None:
            offensive['Ineffective'].append(type_)
        elif a[t] == -1:
            offensive['Not Very Effective'].append(type_)
        elif a[t] < -1:
            offensive['Not Very Effective'].append(f'**{type_}**')
        elif a[t] == 1:
            offensive['Super Effective'].append(type_)
        elif a[t] > 1:
            offensive['Super Effective'].append(f'**{type_}**')

    embed = discord.Embed(
        color = discord.Color.dark_teal(),
        title = 'Offensive',
        description = '/'.join([i.capitalize() for i in types]),
        timestamp = datetime.datetime.now()
    )
    embed.set_thumbnail(url='https://play.pokemonshowdown.com/sprites/types/' + types[0].capitalize() + '.png')
    if offensive['Super Effective'] == []:
        offensive['SuperEffective'].append('None')
    if offensive['Not Very Effective'] == []:
        offensive['Not Very Effective'].append('None')
    if offensive['Ineffective'] == []:
        offensive['Ineffective'].append('None')
    embed.add_field(name='Super Effective', value=', '.join(offensive['Super Effective']), inline=False)
    embed.add_field(name='Not Very Effective', value=', '.join(offensive['Not Very Effective']), inline=False)
    embed.add_field(name='Ineffective', value=', '.join(offensive['Ineffective']), inline=False)

    return embed

def get_defensive_matchup(types):
    b = defensive_matchup(types)

    defensive = {'Weaknesses': [], 'Resistances': [], 'Immunities': []}
    for t in TYPES:
        type_ = t.capitalize()
        if b[t] is None:
            defensive['Immunities'].append(type_)
        elif b[t] == -1:
            defensive['Resistances'].append(type_)
        elif b[t] < -1:
            defensive['Resistances'].append(f'**{type_}**')
        elif b[t] == 1:
            defensive['Weaknesses'].append(type_)
        elif b[t] > 1:
            defensive['Weaknesses'].append(f'**{type_}**')

    embed = discord.Embed(
        color = discord.Color.dark_teal(),
        title = 'Defensive',
        description = '/'.join([i.capitalize() for i in types]),
        timestamp = datetime.datetime.now()
    )
    embed.set_thumbnail(url='https://play.pokemonshowdown.com/sprites/types/' + types[0].capitalize() + '.png')
    if defensive['Weaknesses'] == []:
        defensive['Weaknesses'].append('None')
    if defensive['Resistances'] == []:
        defensive['Resistances'].append('None')
    if defensive['Immunities'] == []:
        defensive['Immunities'].append('None')
    embed.add_field(name='Weaknesses', value=', '.join(defensive['Weaknesses']), inline=False)
    embed.add_field(name='Resistances', value=', '.join(defensive['Resistances']), inline=False)
    embed.add_field(name='Immunities', value=', '.join(defensive['Immunities']), inline=False)

    return embed

# note to future self: also add functionality to look up a pokemon's type