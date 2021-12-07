from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def main():
    driver = webdriver.Firefox()  # abre uma nova instância do navegador
    time.sleep(2)
    driver.get("https://www.google.com.br")  # acessa a página
    time.sleep(2)
    elem = driver.find_element_by_tag_name("input")  # Acha a caixa de busca
    elem.clear()  # limpa o texto anteriormente escrito nela - se existir
    time.sleep(2)
    elem.send_keys("dj andré marques manda AQUELE ao vivo")  # escreve um texto na caixa de busta
    time.sleep(2)
    elem.send_keys(Keys.RETURN)  # aperta enter
    time.sleep(2)
    driver.close()  # fecha a janela do navegador


if __name__ == '__main__':
    main()
