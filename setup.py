import os
import requests
import datetime
from bs4 import BeautifulSoup

date_object = datetime.date.today()

h = {
    "user-agents":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}

url = "https://www.contextotucuman.com/"

resp = requests.get(url, headers=h)

soup = BeautifulSoup(resp.text)

noticias_container = soup.find(id="boxprincipal")
noticias_individual = noticias_container.find_all(class_="thumbnail")

for n in noticias_individual:
    titulo = n.find("a").text
    links = n.find("a", href=True)
    file = open("titulosPrincipales.txt","a")
    file.write("DIARIO DIGITAL CONTEXTO - TUCUMAN: " + str(date_object) + "\n")
    file.write(titulo + "\n" + "\n")
    file.write("MIRA LA NOTICIA COMPLETA AQUI: " + str(links["href"]) + "\n" + "\n" + "\n" + "\n")
    file.close()