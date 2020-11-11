import requests
from bs4 import BeautifulSoup

"""
def get():
    page = requests.get("https://www.babynamewizard.com/the-top-1000-baby-names-of-2017-united-states-of-america")
    soup = BeautifulSoup(page.text, "html.parser")
    names = []    
    
    for tag in soup.find_all("td"):
        tag = tag.get_text()
        try:
            int(tag)
        except:
            if "(" in tag or "," in tag:
                continue
            names.append(tag)
            
    return names
"""    
    
def generate():
    f = open("input/first_names.txt", "r")
    names = f.read().split("//")
    names.pop(-1)
    return names
