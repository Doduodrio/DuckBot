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

def get_matchup(type1, type2):
    # type matchup of type1 used on type2
    return TYPE_CHART[TYPES.index(type2)][TYPES.index(type1)]

def defensive_matchup(types):
    # defensive type matchups of type2
    output = {'bug': 0, 'dark': 0, 'dragon': 0, 'electric': 0, 'fairy': 0, 'fighting': 0, 'fire': 0, 'flying': 0, 'ghost': 0, 'grass': 0, 'ground': 0, 'ice': 0, 'normal': 0, 'poison': 0, 'psychic': 0, 'rock': 0, 'steel': 0, 'water': 0}
    for type1 in TYPES:
        for type2 in types:
            matchup = get_matchup(type1, type2)
            try:
                if matchup == 1:
                    output[type2] -= 1
                elif matchup == 2:
                    output[type2] += 1
                elif matchup == 3:
                    output[type2] = None
            except:
                break
    return output

def offensive_matchup(types):
    # offensive type matchups of type1
    output = {'bug': 0, 'dark': 0, 'dragon': 0, 'electric': 0, 'fairy': 0, 'fighting': 0, 'fire': 0, 'flying': 0, 'ghost': 0, 'grass': 0, 'ground': 0, 'ice': 0, 'normal': 0, 'poison': 0, 'psychic': 0, 'rock': 0, 'steel': 0, 'water': 0}
    for type2 in TYPES:
        for type1 in types:
            matchup = get_matchup(type1, type2)
            try:
                if matchup == 1:
                    output[type2] -= 1
                elif matchup == 2:
                    output[type2] += 1
                elif matchup == 3:
                    output[type2] = None
            except:
                break
    return output

# note to future self: also add functionality to look up a pokemon's type