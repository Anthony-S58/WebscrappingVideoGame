#web scrapping jeux videos

#installer les librairies
#pip install requests
#pip install beautifulsoup4
#pip install pandas

import requests
from bs4 import BeautifulSoup
import pandas as pd

#saisir l'URL
url="https://www.jeuxvideo.com/jeux/jeu-1056358/"
response = requests.get(url)


