from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

# Configura Selenium con el controlador de Chrome
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

# URL del sitio web
url = "https://pokemon.gameinfo.io/es"

# Abre la página en el navegador
driver.get(url)

# Espera unos segundos para que el contenido se cargue completamente (ajusta según tu conexión)
time.sleep(5)

# Busca todos los elementos que contienen los Pokémon
pokemon_elements = driver.find_elements(By.XPATH, "//div[@class='pokemon-list']//a[contains(@class, 'pokemon')]")

# Recorremos cada Pokémon en la lista y extraemos el nombre y el enlace
print("Pokémon encontrados:" + str(len(pokemon_elements)))
for pokemon in pokemon_elements:
    nombre = pokemon.get_attribute("data-name-en")  # Extrae el nombre desde el atributo 'data-name-en'
    enlace = pokemon.get_attribute("href")  # Extrae el enlace del atributo 'href'

    print(f"Nombre: {nombre}, Enlace: {enlace}")

# Cierra el navegador
driver.quit()
