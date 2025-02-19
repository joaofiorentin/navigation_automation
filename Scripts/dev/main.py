from selenium import webdriver
import time

navegador = webdriver.Chrome()

navegador.get("https://selenium-python.readthedocs.io/")
navegador.maximize_window()
notes = navegador.find_element("class name", "reference-internal") 
notes.click()    

time.sleep(10)