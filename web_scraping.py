from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

web_page = response.text
my_soup = BeautifulSoup(web_page, "html.parser")
get_titles = my_soup.find_all(name="h3", class_="title")
titles = []

for title in get_titles:
    titles.append(title.getText())

file = open("web_scraping_titles.txt", mode="a", encoding="utf-8")

for title in titles[::-1]:
    file.write(title + '\n')


file.close()
