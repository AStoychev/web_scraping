import re

import requests
from bs4 import BeautifulSoup

link = requests.get('https://www.meteoblue.com/en/weather/week/42.522N24.734E')

soup = BeautifulSoup(link.content, "html.parser")

temperature = soup.find("tr", class_="temperatures").text.split()[2::]
wind_direction = soup.find("tr", class_="winddirs no-mobile").text.split()[2::]
raw_wind_speed = soup.find("tr", class_="windspeeds")

for row in raw_wind_speed("div", attrs={"class": "cell no-desktop"}):
    print(row.text.strip())