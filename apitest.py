
import sys
import json
import requests
from bs4 import BeautifulSoup4

#json_open = open('/Users/yas/Desktop/VSCode-Python/SampleOffice/cpu.json', 'r')
#data2 = json.load(json_open)

url = "https://google.com"
res = requests.get(url)
soup = BeautifulSoup(res, 'html.parser')
print(soup)

#for v in range(0, len(data2)):
#    print(data2['host'][v]['cpu_type'])
#    print(data2['host'][v]['cpu_model'])