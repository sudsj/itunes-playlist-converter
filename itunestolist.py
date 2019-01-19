from bs4 import BeautifulSoup
import requests

# playlist_link = 'https://itunes.apple.com/in/playlist/bathroom/pl.u-BNA6YjJTRb8x5X7?fbclid=IwAR1SH8y5m4T3zY7h614sevVEfHW8sWXe6nH79aCdQPAPJEoNGt2my8jS0EM'
# list = requests.get(playlist_link).text
# print(list)

saved_list = open("gplist.html", "r")
file = open("playlist.txt", "w")

soup = BeautifulSoup(saved_list, 'lxml')
# print(soup.prettify())
r = soup.find_all("span", class_='we-truncate we-truncate--single-line ember-view tracklist-item__text__headline targeted-link__target')
print(r[0].text.strip())

s = soup.find_all("a", class_='table__row__link table__row__link--secondary')
print(s[0].text.strip())

for song, artist in zip(r,s):
    file.write(song.text.strip() + ' - ' + artist.text.strip() + '\n')
# print(file)
