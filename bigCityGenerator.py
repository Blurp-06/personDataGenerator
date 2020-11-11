import requests
from bs4 import BeautifulSoup

"""
def get():
    page = requests.get("https://www.biggestuscities.com/")
    soup = BeautifulSoup(page.text, "html.parser")
    names = []    
    i = 1
    
    for tag in soup.find_all(class_=["big"]):
        tag = tag.get_text()
        try:
            int(tag)
        except:
            if i % 2 == 0:
                i += 1
                continue
            i += 1
            names.append(tag.strip())
            
    return names
"""

def generate():
    f = open("input/cities.txt", "r")
    names = f.read().split("//")
    names.pop(-1)
    return names