from bs4 import BeautifulSoup
import requests


url = "https://appbrewery.github.io/instant_pot/"
response = requests.get(url)

raw_web_page = response.text

soup = BeautifulSoup(raw_web_page, "html_parser")
get_price = soup.find_all(name="span", class_="a-price-whole")

print(get_price)
