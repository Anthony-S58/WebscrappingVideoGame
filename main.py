#web scrapping jeux videos

#installer les librairies
#pip install requests
#pip install beautifulsoup4
#pip install pandas
#pip install selenium

import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#creer une variable pour declencher le driver
def lauchdriver() :
    driver = webdriver.Chrome()
    driver.get("https://www.jeuxvideo.com")
    return driver

driver = lauchdriver()

#recuperer le bouton pour passer les cookies
searchbar_button = driver.find_element(By.CLASS_NAME, "jad_cmp_paywall_button-cookies")
searchbar_button.click()

