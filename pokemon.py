from databases import Database
import datetime
import discord

db = Database('https://docs.google.com/spreadsheets/d/1qIplFdrzRqHl91V7qRBtsb9LuC1TYW--TFoNlTDvpbA/export?format=tsv&gid=2042923402', 1)

def get_pkmn(pkmn: str):
    pokemon = db.get(pkmn)
    embed = discord.Embed(
        color = discord.Color.dark_teal(),
        title = pokemon[1],
        description = pokemon[2],
        timestamp = datetime.datetime.now()
    )
    embed.set_thumbnail('https://play.pokemonshowdown.com/sprites/bw/' + pokemon[15] + '.png')

    return embed