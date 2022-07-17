from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

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
        # abre uma instância do firefox na página dada
        driver.get("file://" + os.path.join(os.getcwd(), 'dragon_ball.html'))  
        
        print('-----------------------------------------------------')
        print('recuperando um elemento com find_element_by_tag_name:')
        print('-----------------------------------------------------')
        # pega apenas o primeiro <p> da página
        element = driver.find_element_by_tag_name("p")  
        print(element.text)  # imprime o texto do primeiro paraǵrafo
        print('-----------------------------------------------------------')
        print('recuperando vários elementos com find_elements_by_tag_name:')
        print('-----------------------------------------------------------')
        # pega todos os <p> da página
        elements = driver.find_elements_by_tag_name("p")  
        # percorre todos os <p> da página e imprime seu texto
        for some in elements:  
            print(some.text)  
        print('-------------------------------------------------------------')
        print('recuperando vários elementos com find_elements_by_class_name:')
        print('-------------------------------------------------------------')
        # pega todos os <p> da página
        elements = driver.find_elements_by_class_name("strait")  
        for some in elements:  
            print(some.text)  
        print('-----------------------------------------------')
        print('recuperando um elemento com find_element_by_id:')
        print('-----------------------------------------------')
        element = driver.find_element_by_id("lista")
        print('o elemento com id \'lista\' tem a tag <%s>' % (element.tag_name))
        print('-------------------------------------------------')
        print('recuperando elementos com find_elements_by_xpath:')
        print('-------------------------------------------------')
        # pega todos os elementos li seguem o xpath dado - repare
        # que isto tem a ver com a hierarquia dos elementos html
        elements = driver.find_elements_by_xpath('/html/body/ul/li')  
        for some in elements:
            print(some.text)


if __name__ == '__main__':
    main()
