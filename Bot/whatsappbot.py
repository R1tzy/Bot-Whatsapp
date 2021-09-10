#importar as bibliotecas
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
#Navegar até o Whaysapp web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://web.whatsapp.com/")
time.sleep(20) # tempo que ele fica aberto para você conectar o celular no whatsapp web

#Definir contatos e grupos e mensagem a ser enviada
contatos = [""] #coloca o nome do contato para enviar a mensagem
mensagem = "" #Coloca a mensagem que você quer
#Buscar contatos/grupos
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath(
        '//div[contains(@class,"copyable-text selectable-text")]')
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)    

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath(
        '//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)    

for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)
    
#Enviar mensagens para o contato/grupo
