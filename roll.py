import random

def roll(roll_msg: str):
    # generate a list of random numbers from a DND-formatted string

    if 'd' not in roll_msg:
        return

    # guards against asdf case
    roll_msg = roll_msg.split('d')
    try:
        if roll_msg[0]!='':
            num_rolls = int(roll_msg[0])
        else:
            num_rolls = 1
            roll_msg[0] = '1' # fixes bug in line 22, making d24 work
        num_sides = int(roll_msg[1])
    except:
        return

    # guards against d6.0 case
    if ((num_rolls==1 and roll_msg=='') or num_rolls==int(roll_msg[0])) and num_sides==int(roll_msg[1]):
        rolls = []
        for i in range(num_rolls):
            rolls.append(random.randint(1, num_sides))
        return rolls

    return