from bs4 import BeautifulSoup
import requests

def get_article(article_name):
    file = requests.get(f"https://en.wikipedia.org/wiki/{article_name}")
    html = BeautifulSoup(file.content, features="html.parser")
    text = html.find_all(name="p")
    while html.sup:
        html.sup.extract()
    for i in range(len(text)):
        text[i] = ''.join(list(text[i].strings)).strip()
    return text[1]

def get_image(article_name):
    file = requests.get(f"https://en.wikipedia.org/wiki/{article_name}")
    html = BeautifulSoup(file.content, features="html.parser")
    images = html.find_all(name="img")
    if images[3].has_attr("src") and not images[3].has_attr("alt"):
        return "https" + images[3]['src']
    else:
        return None