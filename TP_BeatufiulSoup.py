from bs4 import BeautifulSoup
import requests

#Récupérer le contenu d'une page dans une variable
request_text = requests.get('https://fr.wikipedia.org/wiki/Championnat_de_France_de_football_2019-2020')

#Vérifier la connexion à cette page
print (request_text.status_code)

#Vérifier le contenu de notre variable
# print (request_text.content)

#Formater ce contenu via BeautifulSoup dans une variable pour l'afficher sous un format HTML
soup = BeautifulSoup(request_text.content, 'html.parser')

#print(soup.prettify())

#Afficher les 2 premiers éléments de la page contenu dans une balise <table>
#print (soup.find_all('table', limit=2))

#Afficher le tableau des équipes via leur class
print (soup.find_all('table', class_="wikitable"))

#th_all = soup.find_all('table')
#result =[]
#for th in th_all:
#    result.extend(th.find('table', class_="wikitable sortable jquery-tablesorter"))