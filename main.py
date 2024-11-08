# DuckBot

from dotenv import load_dotenv
import os
import discord

from calc import evaluate
from roll import roll
from pokemon import get_pkmn
from moves import get_move
from abilities import get_ability
from items import get_item
from conditions import get_condition
from natures import get_nature
from type_matchups import get_offensive_matchup, get_defensive_matchup

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  guilds = '\n - '.join([f'{guild.name} (id: {guild.id})' for guild in client.guilds])
  print(f'{client.user} is active in the following guilds:')
  print(f' - {guilds}\n')
  me = client.get_user(587040390603866122)
  await me.send('DuckBot is online')
  print('DuckBot sent a DM to doduodrio (id: 587040390603866122) upon activating!')

@client.event
async def on_message(message):
  # if it's your own message, don't react
  if message.author == client.user:
    return
  # otherwise, react
  msg = message.content.lower().split() # "hElLo!" => "hello!"

  # %ping: reply with pong
  if msg[0] == '%ping':
    await message.channel.send('pong')
    print('\n' + 'DuckBot was pinged')

  # %calc: evaluate an expression
  elif msg[0] == '%calc':
    expression = ''.join(msg[1::])
    try:
      result = evaluate(expression)
      if int(result) == result:
        result = int(result)
    except OverflowError:
      result = 'overflow'
    except:
      result = None
    print('\n' + 'DuckBot evaluated:')
    if result is None:
      await message.channel.send(f'```invalid expression```')
      print('    ' + f'{expression} = invalid expression')
    elif result == 'overflow':
      await message.channel.send(f'```number too large```')
      print('    ' + f'{expression} = number too large')
    else:
      await message.channel.send(f'```{expression} = {result}```')
      print('    ' + f'{expression} = {result}')
  
  # %roll: return random numbers
  elif msg[0] in ['%roll', '%r']:
    print('\n' + 'DuckBot rolled:')
    if len(msg)==1:
      rolls = ', '.join(roll('20d600'))
      await message.channel.send(rolls)
      print('    ' + f'default - {rolls}')
    else:
      roll_msg = msg[1]
      rolls = roll(roll_msg)
      if rolls is not None:
        rolls = ', '.join(rolls)
        await message.channel.send(rolls)
        print('    ' + f'{roll_msg} - {rolls}')
      else:
        await message.channel.send('invalid parameters')
        print('    ' + 'invalid parameters')
  
  # %stats: get pokemon stats
  elif msg[0] == '%stats':
    pkmn = ' '.join(msg[1::])
    print('\n' + 'DuckBot got stats of:')
    try:
      await message.channel.send(embed=get_pkmn(pkmn))
      print('    ' + pkmn)
    except:
      await message.channel.send('error getting pokemon data')
      print('    ' + pkmn + ', but there was an error')
  
  # %move: get move
  elif msg[0] == '%move':
    move = ' '.join(msg[1::])
    print('\n' + 'DuckBot got move data of:')
    try:
      await message.channel.send(embed=get_move(move))
      print('    ' + move)
    except:
      await message.channel.send('error getting move data')
      print('    ' + move + ', but there was an error')
  
  # %ability: get ability
  elif msg[0] == '%ability':
    ability = ' '.join(msg[1::])
    print('\n' + 'DuckBot got ability data of:')
    try:
      await message.channel.send(embed=get_ability(ability))
      print('    ' + ability)
    except:
      await message.channel.send('error getting ability data')
      print('    ' + ability + ', but there was an error')
  
  # %item: get item
  elif msg[0] == '%item':
    item = ' '.join(msg[1::])
    print('\n' + 'DuckBot got item data of:')
    try:
      await message.channel.send(embed=get_item(item))
      print('    ' + item)
    except:
      await message.channel.send('error getting item data')
      print('    ' + item + ', but there was an error')
  
  # %condition: get condition
  elif msg[0] == '%condition':
    condition = ' '.join(msg[1::])
    print('\n' + 'DuckBot got condition data of:')
    try:
      await message.channel.send(embed=get_condition(condition))
      print('    ' + condition)
    except:
      await message.channel.send('error getting condition data')
      print('    ' + condition + ', but there was an error')
  
  # %nature: get nature
  elif msg[0] == '%nature':
    nature = ' '.join(msg[1::])
    print('\n' + 'DuckBot got nature data of:')
    try:
      await message.channel.send(embed=get_nature(nature))
      print('    ' + nature)
    except:
      await message.channel.send('error getting nature data')
      print('    ' + nature + ', but there was an error')
  
  # %type: get type matchup of a list of types
  elif msg[0] in ['%type', '%types']:
    types = ' '.join(msg[1::])
    print('\n' + 'DuckBot got type data of:')
    try:
      types = [i.strip() for i in types.split(',')]
      await message.channel.send(embed=get_offensive_matchup(types))
      await message.channel.send(embed=get_defensive_matchup(types))
      print('    ' + ', '.join(types))
    except:
      await message.channel.send('error getting type data')
      print('    ' + ', '.join(types) + ', but there was an error')

client.run(TOKEN)