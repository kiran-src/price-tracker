from bs4 import BeautifulSoup
import requests

site = requests.get("https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463")
soup = BeautifulSoup(site.text, "html.parser")

print(soup)
print("AAAAAAAAAAAAAAAAAAAA")
print(site.text)