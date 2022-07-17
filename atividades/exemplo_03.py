from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
import time
import os


def main():
    if os.name == 'nt':  # se o sistema operacional for windows
        path = './geckodriver.exe'  # o executável é .exe
    else:  # se o sistema operacional for linux ou mac
        path = './geckodriver'  # o executável não tem extensão

    with webdriver.Firefox(executable_path=path) as driver:
        time.sleep(2)
        driver.get("https://www.google.com.br")  # acessa a página
        time.sleep(2)

        botao_pesquisar = None
        caixa_entrada = None

        inputs = driver.find_elements_by_tag_name("input")
        for some_input in inputs:
            if some_input.get_property('value').lower() == 'pesquisa google':
                botao_pesquisar = some_input
            if some_input.get_property('type').lower() == 'text':
                caixa_entrada = some_input

        caixa_entrada.clear()  # limpa o texto anteriormente escrito nela - se existir
        time.sleep(2)
        caixa_entrada.send_keys("dj andré marques manda AQUELE ao vivo")  # escreve um texto na caixa de busta
        # time.sleep(2)  # TODO descomente para o exercício 5
        botao_pesquisar.click()
        time.sleep(2)


if __name__ == '__main__':
    main()
