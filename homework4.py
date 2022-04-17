import requests
from bs4 import BeautifulSoup

URL = 'https://frsah.ro/calendar/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
stage_table = soup.find(class_='wptb-preview-table wptb-element-main-table_setting-18262')
competitions_rows = stage_table.find_all(class_='wptb-row')
#print(competitions_rows)
competitions = []
for competition in competitions_rows:
    competition_cell = competition.find('p')
    competition_name = competition_cell.text.strip()
    competitions.append(competition_name)

print(*competitions, sep ='\n')

print('Introduceti o noua competitie: \n')
competitions.append(input())
print(*competitions, sep='\n')
