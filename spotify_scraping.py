from bs4 import BeautifulSoup
import requests

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
url = "https://www.billboard.com/charts/hot-100/" + date
response = requests.get(url=url, headers=header)
soup = BeautifulSoup(response.text, 'html.parser')

raw_song_titles = soup.select("li ul li h3")
song_titles = []

for title in raw_song_titles:
    song_titles.append(title.getText().strip())

print(song_titles)



