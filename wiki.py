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