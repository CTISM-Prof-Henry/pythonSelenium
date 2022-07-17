from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

from selenium.webdriver.remote.webelement import WebElement


def main():
    if os.name == 'nt':  # se o sistema operacional for windows
        path = './geckodriver.exe'  # o executável é .exe
    else:  # se o sistema operacional for linux ou mac
        path = './geckodriver'  # o executável não tem extensão

    # usar with garante que o método driver.close() será chamado,
    # mesmo que uma exceção ocorra no meio do código
    # isso evita que, quando fazemos testes e o programa dá erro,
    # fique uma instância do firefox aberta
    with webdriver.Firefox(executable_path=path) as driver:
        time.sleep(2)
        driver.get("https://www.google.com.br")  # acessa a página
        time.sleep(2)
        elements = driver.find_elements_by_tag_name("input")  # Acha a caixa de busca
        for elem in elements:  # type: WebElement
            # procura a caixa de busca do google. Inspecionando ela pelo navegador, descobrimos que ela é
            # (resumidamente)
            # <input name="q" type="text" title="Pesquisar" value="" aria-label="Pesquisar" >
            # portanto, estamos procurando um objeto HTML do tipo input que tenha como título a palavra 'Pesquisar'
            if elem.get_property('title').lower() == 'pesquisar':
                elem.clear()  # limpa o texto anteriormente escrito nela - se existir
                time.sleep(2)
                # escreve um texto na caixa de busta
                elem.send_keys("dj andré marques manda AQUELE ao vivo")
                time.sleep(2)
                elem.send_keys(Keys.RETURN)  # aperta enter
                time.sleep(6)
                break


if __name__ == '__main__':
    main()
