# DuckBot
from dotenv import load_dotenv
import os
import discord

from calc import evaluate

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
  msg = message.content.lower() # "hElLo!" => "hello!"

  if msg == "%ping":
    await message.channel.send('pong')
    print('\n' + 'DuckBot was pinged')
  elif msg.startswith("%calc "):
    expression = ''.join(msg.strip("%calc ").split())
    result = round(float(evaluate(expression))*1000000)/1000000
    if result!="invalid expression":
      await message.channel.send(f'```{expression} = {result}```')
    else:
      await message.channel.send(f'```{result}```')
    print('\n' + f'DuckBot evaluated:')
    print('    ' + f'{expression} = {result}')

client.run(TOKEN)