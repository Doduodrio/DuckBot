import random

def roll(roll_msg: str):
    # generate a list of random numbers from a DND-formatted string

    if 'd' not in roll_msg:
        return

    roll_msg = roll_msg.split('d')
    num_rolls = roll_msg[0]
    num_sides = roll_msg[1]
    rolls = []

    for i in range(num_rolls):
        rolls.append(random.random(1, num_sides+1))
    
    return rolls