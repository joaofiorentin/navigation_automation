from selenium import webdriver
from bs4 import BeautifulSoup
import time

navegador = webdriver.Chrome()

navegador.get("https://selenium-python.readthedocs.io/")
navegador.maximize_window()
notes = navegador.find_element("class name", "reference-internal") 
notes.click()

time.sleep(5)

html = navegador.page_source
soup = BeautifulSoup(html, "html.parser")

elements = soup.find_all("a", class_="reference internal")
for element in elements:
    print("Texto:", element.get_text())
    print("URL:", element.get("href"))

headers = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
for header in headers:
    print("Cabeçalho:", header.get_text())

paragraphs = soup.find_all("p")
for paragraph in paragraphs:
    print("Parágrafo:", paragraph.get_text())

navegador.quit()
