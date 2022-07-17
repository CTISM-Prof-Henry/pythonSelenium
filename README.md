# Selenium

## Sumário

* [Introdução](#introdução)
* [Instalação](#instalação)
* [Métodos de busca](#métodos-de-busca)
* [Exercícios](#exercícios)

## Introdução

Selenium é uma biblioteca escrita em Python para automação de testes 
unitários. Quando construímos sites para Web (usando as tecnologias HTML, CSS e
Javascript), por vezes precisamos testar se os itens da interface gráfica estão 
funcionando. Por exemplo, quando apertamos o botão de login no site, ele 
realmente faz login?

Foi para evitar que as empresas gastem dinheiro com testadores humanos (pessoas
que ficam clicando em todos os lugares de um site, sem parar, por dias a fio)
que selenium foi proposto.

Dado que selenium manipula a parte gráfica dos sites da Web através do DOM - 
[Document Object Model](
https://developer.mozilla.org/pt-BR/docs/Web/API/Document_Object_Model/Introduction),
também é possível utilizá-lo para programar _web crawlers_, programas de 
computador que vasculham sites coletando informações.

(**nota rápida:** DOM é a maneira como páginas Web são organizadas, de maneira 
que programas consigam interagir com elas, como por exemplo um script programado
em Javascript, ou o próprio selenium).

É possível usar o DOM a partir de qualquer navegador, abrindo as ferramentas
de desenvolvedor (geralmente a tecla F12), e selecionando a aba _console_.

## Instalação

Estas instruções são voltadas para a realização dos exercícios, mas também servem
para qualquer código-fonte que você venha a desenvolver que use a biblioteca 
selenium.

1. Clone este repositório na sua máquina
2. [Crie um ambiente virtual do anaconda para trabalhar](
   https://github.com/CTISM-Prof-Henry/pythonEssentials/blob/main/chapters/venvs.md)
3. Instale a bibloteca _selenium_: `conda install selenium --yes`
4. Baixe o [GeckoDriver](https://github.com/mozilla/geckodriver/releases),
   na versão do seu sistema operacional (muito provavelmente Windows, então
   será o arquivo que termina com `win64.zip`)
   e coloque-o na pasta onde está o script que você vai rodar (por exemplo,
   dentro de `atividades` para os exercícios, ou na pasta principal para 
   `dragon_ball.py`)
   * Você também pode colocar GeckoDriver em qualquer pasta, e adicionar o caminho
     para o executável no PATH do sistema.

## Métodos de busca

Quando trabalhando com selenium, existem os seguintes métodos para buscar itens
numa página web:

* `driver.find_element_by_id`
* `driver.find_element_by_class_name` (e sua variante `driver.find_elements_by_class_name`)
* `driver.find_element_by_tag_name` (e sua variante `driver.find_elements_by_tag_name`)
* `driver.find_element_by_xpath` (e sua variante `driver.find_elements_by_xpath`)

Existem outras maneiras, mas estas são as mais usadas. 
[Esta página](https://selenium-python.readthedocs.io/locating-elements.html) 
(em inglês) explica em maiores detalhes todos os métodos.

Considere a página HTML mostrada abaixo, `dragon_ball.html`:

```html
<!DOCTYPE html>
<html>
<head>
   <meta charset="utf-8">
   <title>Dragon Ball</title>
   <style type="text/css">
      .strait {
         width: 400px;
      }
   </style>
</head>
<body>
<h1>Dragon Ball</h1>

<p class="strait">
Dragon Ball é uma franquia de mídia japonesa criada por Akira Toriyama. 
Originalmente iniciada com uma série de mangá escrita e ilustrada por 
Toriyama, foi serializada em capítulos na revista Weekly Shonen Jump de 
1984 a 1995. Os 519 capítulos foram compilados em 42 volumes e 
publicados pela editora Shueisha.
</p>

<img class="strait" src="imagens/goku.jpg">

<h2>Curiosidades</h2>

<ul class="strait">
   <li>Foi inspirado por um mangá que Toriyama escreveu antes, Dragon Boy</li>
   <li>Dragon Ball Z se chama assim pois Toriyama queria que a série terminasse</li>
   <li>Kamehameha é o nome do primeiro rei do Havaí.</li>
</ul>

<p>Para saber mais, acesse o link na 
<a href="https://pt.wikipedia.org/wiki/Dragon_Ball_(s%C3%A9rie)">Wikipédia</a>.
</p>

</body>
</html>
```

O seguinte código em Python recupera diversos itens dela:

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

def main():
    if os.name == 'nt':
        path = './geckodriver.exe'
    else:
        path = './geckodriver'

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

```

O código está disponível no arquivo [dragon_ball.py](dragon_ball.py).

## Exercícios

1. Execute o script [atividades/example_01.py](atividades/example_01.py), a
   partir da pasta `atividades`
    * O que acontece quando o código é executado?
2. Execute o script [atividades/example_02.py](atividades/example_02.py).
    * Qual a diferença dele para o exemplo_01?
    * Abra a página do [Google](https://google.com.br). Sobre o botão 
      "Pesquisa Google", clique com o botão direito e selecione a opção 
      "Inspecionar". No console que se abre, na aba "Elements", procure pela 
      propriedade `value`. O que está escrito nesta propriedade?
      Como isto se relaciona com o que está escrito no código do example_02?
3. Descomente o comentário do exemplo_02 da linha 25. Execute o código novamente. 
   Qual a mensagem de erro que aparece no console? Por que isso ocorre?
4. Por que os programadores que fazem testes com Selenium enchem o código-fonte 
   de `time.sleep`?
5. Modifique o exemplo_02 de forma que o código em Python abra o primeiro link 
   retornado pela busca.
