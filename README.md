# Selenium

Selenium é um framework escrito em Python para automação de testes unitários.

Selenium faz uso do DOM -- [Document Object Model](https://developer.mozilla.org/pt-BR/docs/Web/API/Document_Object_Model/Introduction)
para navegar pela Web, interagindo com os elementos HTML da página.

## Instruções

1. Clone este repositório na sua máquina.
2. Abra a linha de comando.
3. Digite `conda create --name test`. 
    * Caso perguntado para prosseguir, diga que sim (pressione `y` e então `ENTER`)
4. Ative o ambiente virtual: `conda activate test`
5. Instale a bibloteca _selenium_: `conda install selenium`
    * Caso perguntado para prosseguir, diga que sim (pressione `y` e então `ENTER`)
6. Baixe o [GeckoDriver](https://github.com/mozilla/geckodriver/releases) e coloque-o na pasta `examples`

## Exercícios

1. Execute o script [examples/example_01.py](examples/example_01.py), a partir da pasta `examples`
    * O que acontece quando o código é executado?
2. Execute o script [examples/example_02.py](examples/example_02.py).
    * Qual a diferença dele para o exemplo_01?
    * Abra a página do [Google](https://google.com.br). Sobre o botão "Pesquisa Google", clique com o botão direito e selecione a
      opção "Inspecionar". No console que se abre, na aba "Elements", procure pela propriedade `value`. O que está escrito nesta propriedade?
      Como isto se relaciona com o que está escrito no código do example_02?
3. Descomente o comentário do exemplo_02 da linha 25. Execute o código novamente. Qual a mensagem de erro que aparece no
   console? Por que isso ocorre?
4. Por que os programadores que fazem testes com Selenium enchem o código-fonte de `time.sleep`?
5. Modifique o exemplo_02 de forma que o código em Python abra o primeiro link retornado pela busca.
