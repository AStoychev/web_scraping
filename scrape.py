import requests
from bs4 import BeautifulSoup

link = requests.get('https://www.meteoblue.com/en/weather/week/42.522N24.734E')

soup = BeautifulSoup(link.content, "html.parser")

temperature = soup.find("tr", class_="temperatures").text.split()[2::]
wind_direction = soup.find("tr", class_="winddirs no-mobile").text.split()[2::]

'''
This is pure html which consist data from wind speed this data is 
import in format wind speed file wheredata for wind speed is format
and import in scrape in meters per seconds
'''

raw_wind_speed = soup.find("tr", class_="windspeeds")

'''Rain type have two chooses when probability to rain is high html
change class name so this is the reason for create this list'''

rain_type = ["precipprobs no-mobile", "precipprobs no-mobile no-rain"]
rain = soup.find("tr", class_=[x for x in rain_type if x in rain_type]).text.split()[2::]