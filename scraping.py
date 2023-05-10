import os
import time
import json
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')

# Configuracion de descarga

# Obtiene la ruta del script, para que la carpeta de descarga sea relativa a la ubicacion del script
script_dir = os.path.dirname(os.path.abspath(__file__))
download_folder = os.path.join(script_dir, "Books_Download")

prefs = {
    "download.default_directory": download_folder,  # Cambia la carpeta de descarga
    "plugins.always_open_pdf_externally": True  # Para abrir el PDF en un visor externo
}
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)

driver.get('https://freeditorial.com/en')
driver.maximize_window()


# ⚠️ Paginacion 
# para hacer la paginacion hay que revisar la presencia de un <a> con el att "rel" = "next"

# input("Presione enter para continuar")

status_log = {}

try:
    search_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[@href="#ex2"]'))
    )
    search_button.click()
    print("Se encontro el boton de busqueda")
except:
    print("No se encontro el boton de busqueda")
    driver.quit()

# input("Presione enter para continuar")

# click en input search
# search_input = driver.find_element.By.XPATH('//input[@id="search"]')

try:
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@id="search"]'))
    )
    search_input.click()
    print("Se encontro el input de busqueda")
except:
    print("No se encontro el input de busqueda")
    driver.quit()

# input("Presione enter para continuar")

# escribir en input search
search_input.send_keys("Arik Eindrok")

# input("Presione enter para continuar")

# click en boton search
try:
    search_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]'))
    )
    search_button.click()
    print("Se encontro el boton de busqueda")
except:
    print("No se encontro el boton de busqueda")
    driver.quit()

# input("Presione enter para continuar")

# esperar a que carguen todos los libros del autor con xpath

# //article[@class="expandbook"]

try:
    books = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//article[@class="expandbook"]'))
    )
    print("Se encontraron los libros")
except:
    print("No se encontraron los libros")
    driver.quit()

# input("Presione enter para continuar")

# obtener los links de los libros
# //p[@class="book__title"]/a[@href="/en/books/nostalgica-contradiccion"]

links = []
for book in books:
    link = book.find_element(By.XPATH, './/p[@class="book__title"]/a')
    links.append(link.get_attribute("href"))

print(links)

# input("Presione enter para continuar")

# Paginar agregando links hasta que no haya mas links

# //a[@rel="next"]

while True:
    try:
        next_page = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//a[@rel="next"]'))
        )
        next_page.click()
        print("Se encontro el boton de paginacion")
    except:
        print("No se encontro el boton de paginacion")
        break

    try:
        books = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//article[@class="expandbook"]'))
        )
        print("Se encontraron los libros")
    except:
        print("No se encontraron los libros")
        driver.quit()

    for book in books:
        link = book.find_element(By.XPATH, './/p[@class="book__title"]/a')
        links.append(link.get_attribute("href"))

    print(links)

    # input("Presione enter para continuar")

# ir a cada link y obtener los datos

for link in links:
    driver.get(link)
    # input("Presione enter para continuar")

    # click en boton de descarga
    try:
        download_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="links"]//a[contains(@onclick, "downloadbookepub?format2=pdf")]'))
        )
        download_button.click()
        print("Se encontro el boton de descarga")
        status_log[link] = "success"

        # esperar a que se descargue el libro
        # sleep(5)
    except:
        print("No se encontro el boton de descarga")
        status_log[link] = "fail"
        pass

    # input("Presione enter para continuar")

print(status_log)







