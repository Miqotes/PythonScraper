# import module

import requests
from bs4 import BeautifulSoup
import json

url = https://www.trycaviar.com/home/

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

