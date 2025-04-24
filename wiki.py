import datetime
import discord

from bs4 import BeautifulSoup
import requests

def get_article_text(html: BeautifulSoup):
    text = html.find_all(name="p")
    while html.sup:
        html.sup.extract()
    for i in range(len(text)):
        text[i] = ''.join(list(text[i].strings)).strip()
    return text[1]

def get_article_image(html: BeautifulSoup):
    images = html.find_all(name="img")
    for image in images:
        if (image.has_attr("alt") and (image['alt']=="Featured article")):
            return "https" + images[3]['src']
        else:
            return None

def get_article(article_name):
    file = requests.get(f"https://en.wikipedia.org/wiki/{article_name}")
    html = BeautifulSoup(file.content, features="html.parser")
    embed = discord.Embed(
        color = discord.Color.dark_teal(),
        title = article_name,
        description = get_article_text(html),
        url = f"https://en.wikipedia.org/wiki/{article_name}",
        timestamp = datetime.datetime.now()
    )
    embed.set_thumbnail(url=get_article_image(html))
    return embed

# <img src="" decoding="async" width="250" height="275" class="mw-file-element" srcset="" data-file-width="340" data-file-height="374">
# <img src="" decoding="async" width="190" height="250" class="mw-file-element" srcset="" data-file-width="2898" data-file-height="3807">
# <img src="" decoding="async" width="20" height="20" class="mw-file-element" srcset="" data-file-width="512" data-file-height="512">
# <img alt="" class="mw-file-element" data-file-height="391" data-file-width="391" decoding="async" height="27" src="" srcset="" width="27"/>
# <img alt="Page semi-protected" src="" decoding="async" width="20" height="20" class="mw-file-element" srcset="" data-file-width="512" data-file-height="512">
# <img alt="" class="mw-file-element" data-file-height="391" data-file-width="391" decoding="async" height="27" src="" srcset="" width="27"/>