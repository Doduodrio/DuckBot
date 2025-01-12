from bs4 import BeautifulSoup
import datetime
import discord
import requests

gens = [
    ['Red(JPN)', 'Green', 'Red(ENG)', 'Blue', 'Yellow', 'Stadium'],
    ['Gold', 'Silver', 'Crystal', 'Stadium 2'],
    ['Ruby', 'Sapphire', 'Emerald', 'FireRed', 'LeafGreen'],
    ['Diamond', 'Pearl', 'Platinum', 'HeartGold', 'SoulSilver'],
    ['Black', 'White', 'Black 2', 'White 2'],
    ['X', 'Y', 'Omega Ruby', 'Alpha Sapphire'],
    ['Sun', 'Moon', 'Ultra Sun', 'Ultra Moon', "Let's Go Pikachu", "Let's Go Eevee"],
    ['Sword', 'Shield', 'Brilliant Diamond', 'Shining Pearl', 'Legends: Arceus'],
    ['Scarlet', 'Violet']
]

def get_all_text(tag):
    text = ""
    for i in tag.descendants:
        if i.name is None and i.string is not None:
            text += i.string
        elif i.name == "br":
            text += '\n'
    return text.strip()

def is_game_name(tag):
    return tag.has_attr('style') and ("width: 80px; max-width: 80px;" in tag['style']) and ("line-height:12pt;" in tag['style'])

def get_entries(pkmn):
    file = requests.get(f"https://bulbapedia.bulbagarden.net/wiki/{pkmn}_(Pok%C3%A9mon)")
    html = BeautifulSoup(file.content, features="html.parser")

    # get table of pokedex entries (two siblings after h3)
    entry_table = html.find(id="Pok.C3.A9dex_entries").parent.next_sibling.next_sibling

    # extract text from tag objects
    game_tags = entry_table.find_all(is_game_name)
    entries = {}
    last_entry = ""
    for game in game_tags:
        try:
            # do not overwrite base form if you encounter alternate form
            if get_all_text(game) not in entries:
                entries[get_all_text(game)] = get_all_text(game.next_sibling.next_sibling)
                last_entry = get_all_text(game.next_sibling.next_sibling)
        except:
            # copy last entry if entry is None (for when multiple games share an entry)
            entries[get_all_text(game)] = last_entry
    return entries

def get_entries_embed(gen, pkmn):
    entries = get_entries(pkmn)
    embed = discord.Embed(
        color = discord.Color.dark_teal(),
        title = f"{pkmn}'s Pokédex Entries",
        description = '',
        timestamp = datetime.datetime.now()
    )
    if requests.get(url=f"https://play.pokemonshowdown.com/sprites/gen{gen}/{pkmn.lower()}.png"):
        embed.set_thumbnail(url=f"https://play.pokemonshowdown.com/sprites/gen{gen}/{pkmn.lower()}.png")
    elif requests.get(url=f"https://play.pokemonshowdown.com/sprites/dex/{pkmn.lower()}.png"):
        embed.set_thumbnail(url=f"https://play.pokemonshowdown.com/sprites/dex/{pkmn.lower()}.png")
    elif requests.get(url=f"https://play.pokemonshowdown.com/sprites/bw/{pkmn.lower()}.png"):
        embed.set_thumbnail(url=f"https://play.pokemonshowdown.com/sprites/bw/{pkmn.lower()}.png")
    else:
        embed.set_thumbnail(url="https://archives.bulbagarden.net/media/upload/8/8e/Spr_3r_000.png")
    for entry in entries:
        if entry in gens[gen-1]:
            embed.add_field(name=entry, value=entries[entry], inline=False)
    
    return embed

"https://play.pokemonshowdown.com/sprites/bw/slowpoke.png"
"https://play.pokemonshowdown.com/sprites/ani/slowpoke.gif"
"https://play.pokemonshowdown.com/sprites/dex/slowpoke.png"