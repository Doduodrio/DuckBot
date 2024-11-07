type_chart = [
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
types = ['bug', 'dark', 'dragon', 'electric', 'fairy', 'fighting', 'fire', 'flying', 'ghost', 'grass', 'ground', 'ice', 'normal', 'poison', 'psychic', 'rock', 'steel', 'water']

def get_matchup(type1, type2):
    # type matchup of type1 used on type2
    return type_chart[types.index(type2)][types.index(type1)]

def defensive_matchup(type2):
    # defensive type matchups of type2
    resist = []
    weak = []
    immune = []
    for type1 in types:
        matchup = get_matchup(type1, type2)
        if matchup == 1:
            resist.append(type1)
        elif matchup == 2:
            weak.append(type1)
        elif matchup == 3:
            immune.append(type1)
    return {'Resistances': resist, 'Weaknesses': weak, 'Immunities': immune}

def offensive_matchup(type1):
    # offensive type matchups of type1
    se = []
    nve = []
    immune = []
    for type2 in types:
        matchup = get_matchup(type1, type2)
        if matchup == 1:
            nve.append(type2)
        elif matchup == 2:
            se.append(type2)
        elif matchup == 3:
            immune.append(type2)
    return {'Super Effective': se, 'Not Very Effective': nve, 'Ineffective': immune}

# note to future self: modify offensive and defensive matchup functions to accept a list of types