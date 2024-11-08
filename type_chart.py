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

def get_matchup(types):
    a = offensive_matchup(types)
    b = defensive_matchup(types)
    offensive = [[], [], []]
    defensive = [[], [], []]
    for t in TYPES: # resume work on this for loop
        if offensive[t] and offensive[t] < offensive[0]:
            offensive[1].append(t)
        else:
            offensive[2].append(t)
    embed = discord.Embed(
        color = discord.Color.dark_teal(),
        title = 'Offensive',
        description = '/'.join(types),
        timestamp = datetime.datetime.now()
    )
    embed.add_field(name='Super Effective', value=', '.join(se), inline=False)
    embed.add_field(name='Not Very Effective', value=', '.join(nve), inline=False)
    embed.add_field(name='Ineffective', value=', '.join(ineffective), inline=False)

# note to future self: also add functionality to look up a pokemon's type