# DuckBot

from dotenv import load_dotenv
import os
import discord

from calc import evaluate
from roll import roll
from pokemon import get_pkmn
from moves import get_move

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
  
  # %stats: get stats of a pokemon
  elif msg[0] == '%stats':
    pkmn = ' '.join(msg[1::])
    print('\n' + 'DuckBot got stats of:')
    try:
      await message.channel.send(embed=get_pkmn(pkmn))
      print('    ' + pkmn)
    except:
      await message.channel.send('error getting pokemon data')
      print('    ' + pkmn + ', but there was an error')
  
  # %move: get move data
  elif msg[0] == '%move':
    move = ' '.join(msg[1::])
    print('\n' + 'DuckBot got move data of:')
    try:
      await message.channel.send(embed=get_move(move))
      print('    ' + move)
    except:
      await message.channel.send('error getting move data')
      print('    ' + move + ', but there was an error')

client.run(TOKEN)