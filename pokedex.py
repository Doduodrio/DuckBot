from bs4 import BeautifulSoup
import requests

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