# Selenium

Selenium é um framework escrito em Python para automação de testes unitários.

Selenium faz uso do DOM -- [Document Object Model](https://developer.mozilla.org/pt-BR/docs/Web/API/Document_Object_Model/Introduction)
para navegar pela Web, interagindo com os elementos HTML da página.

## Exercícios

1. Execute o script [examples/example_01.py](examples/example_01.py).
    * Nota: talvez seja preciso baixar o [ChromeDriver](https://chromedriver.chromium.org/downloads) e colocá-lo na mesma
      pasta deste projeto.
    * O que acontece quando o código é executado?
2. Execute o script [examples/example_02.py](examples/example_02.py).
    * Qual a diferença dele para o exemplo_01?
    * Abra a página do [Google](https://google.com.br). Sobre a caixa de texto, clique com o botão direito e selecione a
      opção "Inspecionar". No console que se abre, procure pela propriedade `value`. O que está escrito nesta propriedade?
      O que isso tem a ver com os nomes que apareceram no código em Python?
3. Descomente o comentário do exemplo_02 da linha 25. Execute o código novamente. Qual a mensagem de erro que aparece no
   console? Por que isso ocorre?
4. Por que os programadores que fazem testes com Selenium enchem o código-fonte de `time.sleep`?
5. Modifique o exemplo_01 de forma que o código em Python abra o primeiro link retornado pela busca.