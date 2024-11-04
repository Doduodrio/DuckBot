# DuckBot

from dotenv import load_dotenv
import os
import discord

from calc import evaluate
from roll import roll

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
    except:
      result = None
    print('\n' + f'DuckBot evaluated:')
    try:
      float(result)
      await message.channel.send(f'```{expression} = {result}```')
      print('    ' + f'{expression} = {result}')
    except OverflowError:
      await message.channel.send(f'```number too large```')
      print('    ' + f'{expression} = number too large')
    except:
      await message.channel.send(f'```invalid expression```')
      print('    ' + f'{expression} = invalid expression')
  
  # %roll: return random numbers
  elif msg == '%roll':
    print('\n' + f'Duckbot rolled:')
    if len(msg)==1:
      await message.channel.send('Cannot roll nothing')
      print('    ' + 'nothing')
    else:
      roll_msg = msg[1]
      rolls = roll(roll_msg)

client.run(TOKEN)