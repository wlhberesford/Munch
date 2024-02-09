import requests
from bs4 import BeautifulSoup

URL = "https://rpi.sodexomyway.com/dining-near-me/hours"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# Find all div elements with class "dining-location"
dining_group = soup.find_all("li", class_="dining-group")

for group in dining_group:
    print(group.text.strip(), end="\n"*2)


