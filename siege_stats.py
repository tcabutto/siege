import bs4
import requests
from bs4 import BeautifulSoup as soup

my_url = 'https://r6stats.com/stats/uplay/Reload316/ranked'
#Will use main ubi site if can bypass browser error




agent = {"User-Agent":"Mozilla/5.0"}
source = requests.get(my_url, headers=agent).text

page_soup = soup(source, 'lxml')
row1 = page_soup.find('div', class_='row stats')
row2 = page_soup.find('div', class_='row stats second')

#Grabbing all the values for each above
vals1 = row1.find_all('div', class_='value')
vals2 = row2.find_all('div', class_='value')

filename = 'r6stats.csv'
f = open(filename, 'w')

headers = "kills, deaths, K/D ratio, playtime, record, win percentage, XP until lvl up, overall level\n"
f.write(headers)

kills       = vals1[0].text.strip()
deaths      = vals1[1].text.strip()
kd          = vals1[2].text.strip()
playtime    = vals1[3].text.strip()
record      = vals2[0].text.strip()
winPercent  = vals2[1].text.strip()
levelUp     = vals2[2].text.strip()
level       = vals2[3].text.strip()

print('Kills: ' + kills)
print('Deaths: ' + deaths)
print('K/D ratio: ' + kd)
print('Playtime: ' + playtime)
print('record: ' + record)
print('winPercent: ' + winPercent)
print('xp until lvl up: ' + levelUp)
print('Overall level: ' + level)

f.write(kills + "," + deaths + "," + kd + "," + playtime + "," + record + "," + winPercent + "," + levelUp.replace(",", "") + "," + level + "\n")
f.close()
