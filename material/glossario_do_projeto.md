# Glossário Completo do Código Python do PDV

Aqui está um glossário completo com as palavras-chave e conceitos do código do PDV, explicados de forma simples, incluindo tudo que está presente no código:

## **Palavras-chave:**

* **`import`:**  Uma palavra-chave que permite importar módulos e bibliotecas Python para usar em seu código. Exemplo: `import print_reprograma as pr`.
* **`from`:**  Uma palavra-chave usada para importar partes específicas de um módulo ou pacote. Exemplo: `from datetime import datetime`.
* **`as`:**  Uma palavra-chave usada para renomear um módulo ou biblioteca importada para um nome mais curto. Exemplo: `import print_reprograma as pr`.
* **`def`:**  Uma palavra-chave usada para definir uma função. Exemplo: `def imprimir_cabecalho(erro):`.
* **`return`:**  Uma palavra-chave usada dentro de uma função para retornar um valor. Exemplo: `return input().lower()`.
* **`if`:**  Uma palavra-chave usada para criar uma condição. Se a condição for verdadeira, o código dentro do bloco `if` é executado. Exemplo: `if(erro != ''):`.
* **`elif`:**  Uma palavra-chave usada para criar uma condição alternativa. Se a condição `if` for falsa, o Python verifica se a condição `elif` é verdadeira. Exemplo: `elif(tela == 'ajuda'):`.
* **`else`:**  Uma palavra-chave usada para criar um bloco de código que será executado se nenhuma das condições `if` ou `elif` for verdadeira. Exemplo: `else:`.
* **`while`:**  Uma palavra-chave usada para criar um loop. O código dentro do loop é executado repetidamente enquanto a condição do loop for verdadeira. Exemplo: `while(opcao != 'q'):`.
* **`try`:**  Uma palavra-chave usada para tentar executar um bloco de código. Exemplo: `try:`.
* **`except`:**  Uma palavra-chave usada para tratar exceções (erros) que podem ocorrer durante a execução do bloco `try`. Exemplo: `except ValueError:`.
* **`for`:**  Uma palavra-chave usada para criar um loop que itera sobre os elementos de uma sequência (como uma lista ou uma string). Exemplo: `for produto in compra:`.
* **`in`:**  Uma palavra-chave usada para verificar se um elemento está presente em uma sequência. Exemplo: `if produto['codigo'] == codigo:`.
* **`print`:**  Uma função usada para exibir texto no terminal. Exemplo: `print(opcao)`.
* **`str`:**  Uma função usada para converter um valor para uma string. Exemplo: `str(produto['codigo'])`.
* **`int`:**  Uma função usada para converter um valor para um inteiro. Exemplo: `int(opcao)`.
* **`round`:**  Uma função usada para arredondar um número para um determinado número de casas decimais. Exemplo: `round(total, 2)`.
* **`len`:**  Uma função que retorna o comprimento de uma sequência (como uma lista ou uma string). Exemplo: `len(compra)`.
* **`append`:**  Um método de lista que adiciona um elemento ao final da lista. Exemplo: `compra.append(novo_produto(produto, 1))`.
* **`replace`:**  Um método de string que substitui todas as ocorrências de um caractere ou substring por outro. Exemplo: `opcao.replace('x', '')`.

## **Conceitos:**

* **Módulo:** Um arquivo Python que contém código, como funções, classes, variáveis e constantes. Exemplo: `print_reprograma.py`.
* **Biblioteca:** Um conjunto de módulos e pacotes pré-escritos que oferecem funcionalidades prontas para uso. Exemplo: `datetime`.
* **Função:** Um bloco de código reutilizável que realiza uma tarefa específica. Exemplo: `imprimir_cabecalho()`.
* **Lista:** Uma estrutura de dados que armazena uma sequência ordenada de elementos. Exemplo: `produtos`, `compra`, `compras`.
* **Dicionário:** Uma estrutura de dados que armazena pares chave-valor. Exemplo: `produtos`, `novo_produto`.
* **Variável:** Um nome que se refere a um valor na memória do computador. Exemplo: `opcao`, `erro`, `tela`, `compra`, `compras`, `quantidade`, `total`, `codigo`, `produto`.
* **Condição:**  Uma expressão que é avaliada como verdadeira ou falsa. Exemplo: `if opcao == 'h':`, `if erro != '':`, `if len(compra) > 0:`.
* **Loop:**  Um bloco de código que é executado repetidamente enquanto uma condição for verdadeira. Exemplo: `while(opcao != 'q'):`, `for produto in compra:`.
* **Exceção:** Um erro que ocorre durante a execução de um programa. Exemplo: `ValueError`.
* **Tratamento de exceções:**  O processo de lidar com erros que podem ocorrer durante a execução do programa. Exemplo: `try: ... except ValueError: ...`.

## **Conceitos específicos do código:**

* **`sv`:**  Um argumento para a função `retangulo()` do módulo `print_reprograma`, que controla o número de espaços vazios em cima e embaixo do texto dentro do retângulo.
* **`tamanho`:** Um argumento para as funções `imprimir()`, `separador()`, `retangulo()`, etc. do módulo `print_reprograma`, que define a largura da linha ou do retângulo.
* **`alinhar`:** Um argumento para as funções `imprimir()`, `retangulo()`, etc. do módulo `print_reprograma`, que define o alinhamento do texto.
* **`caracter`:** Um argumento para as funções `imprimir()`, `separador()`, etc. do módulo `print_reprograma`, que define o caractere a ser usado para preencher espaços ou criar linhas de separação.
* **`end`:** Um argumento para a função `imprimir()`, que define o caractere a ser usado para finalizar a linha.
* **`cor_texto`:** Um argumento para as funções `imprimir()`, `retangulo()`, etc. do módulo `print_reprograma`, que define a cor do texto.
* **`cor_barra`:** Um argumento para a função `retangulo()`, que define a cor da barra do retângulo.
* **`pr.limpar_formatacao()`:**  Uma função do módulo `print_reprograma` que remove a formatação aplicada ao texto (cores e estilos).
* **`pr.pular_linha()`:**  Uma função do módulo `print_reprograma` que imprime uma linha em branco.
* **`pr.limpar()`:**  Uma função do módulo `print_reprograma` que limpa a tela do terminal.

</br>

> Espero que este glossário detalhado ajude a entender melhor o código do PDV! 💜


