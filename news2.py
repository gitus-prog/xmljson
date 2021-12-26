from json import dump
import xml.etree.ElementTree as ET
from urllib.request import urlopen

data = ET.fromstring(urlopen('https://lenta.ru/rss').read().decode('utf8'))
ans = []

for item in data.findall('channel/item'):
    ans.append(
        { item.tag: item.text for j in item }
    )

with open("news_second.json", "w", encoding = 'UTF-8') as file:
    dump(ans, file, indent = 1, ensure_ascii = False)