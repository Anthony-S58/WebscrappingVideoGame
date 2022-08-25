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

game = input("Quel jeu voulez-vous chercher ? ")

#creer une variable pour declencher le driver
def launchdriver() :
    driver = webdriver.Chrome()
    driver.get("https://www.jeuxvideo.com")
    return driver

driver = launchdriver()

#recuperer le bouton pour passer les cookies
cookies_button = driver.find_element(By.CLASS_NAME, "jad_cmp_paywall_button-cookies")
cookies_button.click()
#récupérer le bouton de recherche pour activer la barre de recherche
searchbar_button = driver.find_element(By.CLASS_NAME, "header__navLinkSearch")
searchbar_button.click()
#récupérer la barre de recherche et insérer un texte
search_bar = driver.find_element(By.ID, "search")
search_bar.send_keys(game)
#récupérer le bouton pour valider la recherche et effectuer la recherche
validation_button = driver.find_element(By.CLASS_NAME, "headerSearch__formBtn")
validation_button.click()
#récupérer la catégorie jeux
# game_categorie = driver.find_element(By.CLASS_NAME, "lien-jv")
# game_categorie.click()
game_link = driver.find_element(By.CLASS_NAME, "card__link")
game_link.click()
