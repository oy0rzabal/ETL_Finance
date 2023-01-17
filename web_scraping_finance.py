from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

web = "https://finance.yahoo.com/quote/AXP/history?p=AXP"
path = '/Escritorio/chromedriver'
driver = webdriver.Chrome(path)
driver.get(web)
driver.maximize_window()

# Localizar el contenedor (container) que contiene todos los audiolibros listados en la pagina
container = driver.find_element(By.ID, "Col1-1-HistoricalDataTable-Proxy")
# Obtener todos los audiolibros listados (el "/" da los nodos hijos)
products = container.find_elements(By.XPATH, ".//table[@class='W(100%) M(0)']")
# products = container.find_elements_by_xpath('./li')

# Inicializar el almacenamiento
Date = []
prices = []
# Hacer un "bucle for" a la lista de productos (cada "product" representa un audiolibro)
for product in products:
    # Usamos la funcion "contains" para buscar elementos que contienen un texto en particular, así evitamos construir XPath largos
    Date.append(product.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody').text)  # Almacenando data en la lista

driver.quit()
# Almacenando data en un dataframe y exportando a un archivo CSV
df_books = pd.DataFrame({'info': Date})
df_books.to_csv('books.csv', index=False)
