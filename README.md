# Selenium

## Sumário

* [Introdução](#introdução)
* [Instruções](#instruções)
* [Exercícios](#exercícios)

## Introdução

Selenium é uma biblioteca escrita em Python para automatização de testes 
unitários. Quando construímos sites para Web (usando as tecnologias HTML, CSS e
Javascript), por vezes precisamos testar se as funcionalidades estão funcionando
corretamente. Por exemplo, quando apertamos o botão de login no site, ele 
realmente faz login?

Para estas tarefas, podemos usar selenium, que automatiza o processo de testagem,
e evita que testadores humanos precisem fazer este trabalho monótono e cansativo.

Por manipular a parte gráfica de uma página Web, também é possível usar selenium
para programar _web crawlers_, programas de computador que vasculham sites em 
busca de coletar informações.

Selenium faz uso do DOM - [Document Object Model](
https://developer.mozilla.org/pt-BR/docs/Web/API/Document_Object_Model/Introduction)
para manipular as páginas Web. É possível usar o DOM a partir de qualquer 
navegador, abrindo a aba console, com a tecla F12.

## Instruções

Estas instruções são voltadas para a realização dos exercícios, mas também servem
para qualquer código-fonte que você venha a desenvolver que use a biblioteca 
selenium.

1. Clone este repositório na sua máquina
2. [Crie um ambiente virtual para trabalhar](https://github.com/CTISM-Prof-Henry/pythonEssentials/blob/main/chapters/venvs.md)
3. Instale a bibloteca _selenium_: `conda install selenium --yes`
4. Baixe o [GeckoDriver](https://github.com/mozilla/geckodriver/releases) 
   e coloque-o na pasta `atividades`

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
