import requests
from bs4 import BeautifulSoup

"""
def get():
    page = requests.get("https://namecensus.com/data/10000.html")
    soup = BeautifulSoup(page.text, "html.parser")
    names = []

    for tag in soup.find_all("td"):
        tag = tag.get_text()
        try:
            int(tag)
        except:
            names.append(tag.lower())
    return names
"""

def generate():
    f = open("input/first_names.txt", "r")
    names = f.read().split("//")
    names.pop(-1)
    return names