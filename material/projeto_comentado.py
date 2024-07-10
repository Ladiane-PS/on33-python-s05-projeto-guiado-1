# Olá! Este é um programa que simula um terminal de vendas. 
# Ele permite que você adicione produtos à sua compra, 
# visualize o total, feche a compra e até mesmo encerrar o caixa.


# Importamos a biblioteca print_reprograma para deixar a tela do programa mais bonita!
import print_reprograma as pr  # Podemos usar 'pr' para chamar as funções da biblioteca
# Importamos a biblioteca datetime para trabalhar com datas e horas
from datetime import datetime  # Usaremos esta biblioteca para registrar a data e hora das compras

# Nossa loja tem vários produtos, cada um com um código, nome e preço.
# Veja como os produtos estão organizados:
produtos = [
    {'codigo': 1, 'nome': 'Introdução à Computação - Volume 1', 'valor': 10.00},
    {'codigo': 2, 'nome': 'Introdução à Computação - Volume 2', 'valor': 10.00},
    {'codigo': 3, 'nome': 'Linguagens de Programação Web', 'valor': 10.00},
    {'codigo': 4, 'nome': 'Tecnologias de Scripting', 'valor': 10.00},
    {'codigo': 5, 'nome': 'Desenvolvimento Web com SQL', 'valor': 15.00},
    {'codigo': 6, 'nome': 'Desenvolvimento Web com C++', 'valor': 15.00},
    {'codigo': 7, 'nome': 'Desenvolvimento Web com Java', 'valor': 15.00},
    {'codigo': 8, 'nome': 'Desenvolvimento Web com .Net', 'valor': 15.00},
    {'codigo': 9, 'nome': 'Hardware e Redes de Computadores - Volume 1', 'valor': 15.00},
    {'codigo': 10, 'nome': 'Hardware e Redes de Computadores - Volume 2', 'valor': 15.00},
    {'codigo': 11, 'nome': 'Hardware e Redes de Computadores - Volume 3', 'valor': 15.00},
    {'codigo': 12, 'nome': 'Hardware e Redes de Computadores - Volume 4', 'valor': 15.00},
    {'codigo': 13, 'nome': 'Dominando o Inglês', 'valor': 5.00},
    {'codigo': 14, 'nome': 'Comunicação Empresarial', 'valor': 10.00},
    {'codigo': 15, 'nome': 'Desenvolvimento Pessoal - Livro 1', 'valor': 15.00},
    {'codigo': 16, 'nome': 'Desenvolvimento Pessoal - Livro 2', 'valor': 15.00},
    {'codigo': 17, 'nome': 'Introdução à Computação - Volume 1', 'valor': 10.00},
    {'codigo': 18, 'nome': 'Introdução à Computação - Volume 2', 'valor': 10.00},
    {'codigo': 19, 'nome': 'Fundamentos da Programação', 'valor': 12.00},
    {'codigo': 20, 'nome': 'Algoritmos e Estruturas de Dados', 'valor': 15.00},
    {'codigo': 21, 'nome': 'Introdução à Engenharia de Software', 'valor': 18.00},
    {'codigo': 22, 'nome': 'Banco de Dados', 'valor': 12.00},
    {'codigo': 23, 'nome': 'Programação Web com Python', 'valor': 15.00},
    {'codigo': 24, 'nome': 'Programação Web com JavaScript', 'valor': 15.00},
    {'codigo': 25, 'nome': 'Introdução à Ciência da Computação', 'valor': 18.00},
    {'codigo': 26, 'nome': 'Inteligência Artificial', 'valor': 20.00},
    {'codigo': 27, 'nome': 'Redes de Computadores', 'valor': 15.00},
    {'codigo': 28, 'nome': 'Segurança da Informação', 'valor': 18.00},
    {'codigo': 29, 'nome': 'Administração de Sistemas', 'valor': 15.00},
    {'codigo': 30, 'nome': 'Gestão de Projetos de TI', 'valor': 12.00},
    {'codigo': 31, 'nome': 'Introdução à Estatística', 'valor': 10.00},
    {'codigo': 32, 'nome': 'Probabilidade', 'valor': 10.00},
    {'codigo': 33, 'nome': 'Matemática Discreta', 'valor': 12.00},
    {'codigo': 34, 'nome': 'Cálculo', 'valor': 15.00},
    {'codigo': 35, 'nome': 'Álgebra Linear', 'valor': 12.00},
    {'codigo': 36, 'nome': 'Geometria Analítica', 'valor': 10.00},
    {'codigo': 37, 'nome': 'Física', 'valor': 15.00},
    {'codigo': 38, 'nome': 'Química', 'valor': 12.00},
    {'codigo': 39, 'nome': 'Biologia', 'valor': 10.00},
    {'codigo': 40, 'nome': 'História', 'valor': 10.00},
    {'codigo': 41, 'nome': 'Geografia', 'valor': 10.00},
    {'codigo': 42, 'nome': 'Sociologia', 'valor': 12.00},
    {'codigo': 43, 'nome': 'Filosofia', 'valor': 10.00},
    {'codigo': 44, 'nome': 'Literatura Brasileira', 'valor': 10.00},
    {'codigo': 45, 'nome': 'Literatura Portuguesa', 'valor': 10.00},
    {'codigo': 46, 'nome': 'Literatura Inglesa', 'valor': 10.00},
    {'codigo': 47, 'nome': 'Literatura Espanhola', 'valor': 10.00},
    {'codigo': 48, 'nome': 'Literatura Francesa', 'valor': 10.00},
    {'codigo': 49, 'nome': 'Literatura Alemã', 'valor': 10.00},
    {'codigo': 50, 'nome': 'Literatura Italiana', 'valor': 10.00},
    {'codigo': 51, 'nome': 'Literatura Russa', 'valor': 10.00},
    {'codigo': 52, 'nome': 'Literatura Japonesa', 'valor': 10.00},
    {'codigo': 53, 'nome': 'Literatura Chinesa', 'valor': 10.00},
    {'codigo': 54, 'nome': 'Arte', 'valor': 10.00},
    {'codigo': 55, 'nome': 'Música', 'valor': 10.00},
    {'codigo': 56, 'nome': 'Cinema', 'valor': 10.00},
    {'codigo': 57, 'nome': 'Teatro', 'valor': 10.00},
    {'codigo': 58, 'nome': 'Dança', 'valor': 10.00},
    {'codigo': 59, 'nome': 'Fotografia', 'valor': 10.00},
    {'codigo': 60, 'nome': 'Direito', 'valor': 15.00},
    {'codigo': 61, 'nome': 'Economia', 'valor': 12.00},
    {'codigo': 62, 'nome': 'Administração', 'valor': 10.00},
    {'codigo': 63, 'nome': 'Contabilidade', 'valor': 12.00},
    {'codigo': 64, 'nome': 'Marketing', 'valor': 10.00},
    {'codigo': 65, 'nome': 'Publicidade e Propaganda', 'valor': 10.00},
    {'codigo': 66, 'nome': 'Recursos Humanos', 'valor': 10.00},
    {'codigo': 67, 'nome': 'Relações Públicas', 'valor': 10.00},
    {'codigo': 68, 'nome': 'Comunicação', 'valor': 10.00},
    {'codigo': 69, 'nome': 'Jornalismo', 'valor': 12.00},
    {'codigo': 70, 'nome': 'Psicologia', 'valor': 10.00},
    {'codigo': 71, 'nome': 'Sociologia', 'valor': 10.00},
    {'codigo': 72, 'nome': 'Antropologia', 'valor': 10.00},
    {'codigo': 73, 'nome': 'Ciência Política', 'valor': 10.00},
    {'codigo': 74, 'nome': 'História da Arte', 'valor': 10.00},
    {'codigo': 75, 'nome': 'História da Música', 'valor': 10.00},
    {'codigo': 76, 'nome': 'História do Cinema', 'valor': 10.00},
    {'codigo': 77, 'nome': 'História do Teatro', 'valor': 10.00},
    {'codigo': 78, 'nome': 'História da Dança', 'valor': 10.00},
    {'codigo': 79, 'nome': 'História da Fotografia', 'valor': 10.00},
    {'codigo': 80, 'nome': 'Filosofia da Arte', 'valor': 10.00},
    {'codigo': 81, 'nome': 'Filosofia da Música', 'valor': 10.00},
    {'codigo': 82, 'nome': 'Filosofia do Cinema', 'valor': 10.00},
    {'codigo': 83, 'nome': 'Filosofia do Teatro', 'valor': 10.00},
    {'codigo': 84, 'nome': 'Filosofia da Dança', 'valor': 10.00},
    {'codigo': 85, 'nome': 'Filosofia da Fotografia', 'valor': 10.00},
    {'codigo': 86, 'nome': 'Ética', 'valor': 10.00},
    {'codigo': 87, 'nome': 'Ética Profissional', 'valor': 10.00},
    {'codigo': 88, 'nome': 'Ética e Responsabilidade Social', 'valor': 10.00},
    {'codigo': 89, 'nome': 'Lógica', 'valor': 10.00},
    {'codigo': 90, 'nome': 'Pensamento Crítico', 'valor': 10.00},
    {'codigo': 91, 'nome': 'Introdução ao Direito', 'valor': 15.00},
    {'codigo': 92, 'nome': 'Direito Constitucional', 'valor': 15.00},
    {'codigo': 93, 'nome': 'Direito Civil', 'valor': 15.00},
    {'codigo': 94, 'nome': 'Direito Penal', 'valor': 15.00},
    {'codigo': 95, 'nome': 'Direito Processual', 'valor': 15.00},
    {'codigo': 96, 'nome': 'Direito do Trabalho', 'valor': 15.00},
    {'codigo': 97, 'nome': 'Direito Tributário', 'valor': 15.00},
    {'codigo': 98, 'nome': 'Direito Empresarial', 'valor': 15.00},
    {'codigo': 99, 'nome': 'Direito Internacional', 'valor': 15.00},
    {'codigo': 100, 'nome': 'Direito Ambiental', 'valor': 15.00},
]

# Esta função procura um produto pelo código que você digitar.
# Imagine que você digite o código '1', a função vai encontrar o primeiro produto da lista.
def produto_codigo(codigo):  # Esta função recebe o código do produto como entrada
    # Percorremos a lista de produtos, um por um
    for produto in produtos:  # Para cada produto na lista de produtos
        # Se o código do produto atual for igual ao código que você digitou
        if produto['codigo'] == codigo:  # Se o código do produto for igual ao código que você digitou
            # Encontramos o produto!
            return produto  # Retornamos o produto encontrado

# Esta função cria um novo item para a sua compra.
# Ela pega as informações do produto e a quantidade que você deseja comprar.
def novo_produto(produto, quantidade):  # Esta função recebe o produto e a quantidade como entrada
    # Criamos um novo dicionário para guardar as informações do item da compra
    return {  # Retornamos um novo dicionário
        'codigo': produto['codigo'],  # O código do item é o mesmo do produto
        'nome': produto['nome'],  # O nome do item é o mesmo do produto
        'valor': produto['valor'],  # O valor do item é o mesmo do produto
        'quantidade': quantidade  # A quantidade do item é a que você digitou
    }

# Esta função imprime um resumo de todas as compras do dia.
# Ela mostra a data, a quantidade de itens e o valor total de cada compra.
def imprime_fechamento_caixa(compras):  # Esta função recebe uma lista de compras como entrada
    # Imprimimos o cabeçalho da tabela de compras
    pr.imprimir('Data', tamanho=89, alinhar='centro', end='|')  # Imprimimos a coluna 'Data'
    pr.imprimir('Qt.', tamanho=9, alinhar='centro', end='|')  # Imprimimos a coluna 'Qt.' (quantidade)
    pr.imprimir('valor', tamanho=20, alinhar='centro')  # Imprimimos a coluna 'valor'
    # Inicializamos a variável 'total' para guardar o valor total das compras
    total = 0
    # Percorremos a lista de compras, uma por uma
    for compra in compras:  # Para cada compra na lista de compras
        # Somamos o valor total da compra ao total geral
        total += compra['total']  # Somamos o valor da compra ao total
        # Imprimimos a data da compra
        pr.imprimir(compra['data'].strftime("%d/%m/%Y %H:%M:%S "), tamanho=89, end='|', alinhar='fim')  # Imprimimos a data da compra
        # Imprimimos a quantidade de itens na compra
        pr.imprimir(str(len(compra['itens'])), tamanho=9, end='|', alinhar='centro')  # Imprimimos a quantidade de itens
        # Imprimimos o valor total da compra
        pr.imprimir('R$', str(round(compra['total'], 2)), tamanho=20, alinhar='fim')  # Imprimimos o valor total da compra
    # Imprimimos uma linha separadora
    pr.separador(120, caracter='-')  # Imprimimos uma linha separadora
    # Imprimimos o valor total das compras do dia
    pr.imprimir('Total de compras do caixa', tamanho=99, alinhar='fim', end='|')  # Imprimimos o total das compras
    pr.imprimir('R$', str(round(total, 2)), tamanho=20, alinhar='fim')  # Imprimimos o valor total das compras

# Esta função imprime uma compra fechada, mostrando todos os itens e o total a pagar.
def imprime_compra_fechada(compra, total):  # Esta função recebe a compra e o valor total como entrada
    # Inicializamos a variável 'total_compra' para guardar o valor total da compra
    total_compra = 0
    # Imprimimos o cabeçalho da tabela de produtos da compra
    pr.imprimir('codigo', tamanho=6, alinhar='centro', end='|')  # Imprimimos a coluna 'codigo'
    pr.imprimir('produto', tamanho=83, alinhar='centro', end='|')  # Imprimimos a coluna 'produto'
    pr.imprimir('qtd', tamanho=3, alinhar='centro', end='|')  # Imprimimos a coluna 'qtd' (quantidade)
    pr.imprimir('valor un.', tamanho=12, alinhar='centro', end='|')  # Imprimimos a coluna 'valor un.' (valor unitário)
    pr.imprimir('valor', tamanho=12, alinhar='centro')  # Imprimimos a coluna 'valor' (valor total)
    # Percorremos a lista de produtos da compra, um por um
    for produto in compra:  # Para cada produto na lista de produtos
        # Imprimimos as informações do produto
        imprimir_produto(produto)  # Chamamos a função 'imprimir_produto' para imprimir as informações do produto
        # Calculamos o valor total do produto
        total_compra += produto['valor'] * produto['quantidade']  # Somamos o valor total do produto ao total da compra
    # Imprimimos uma linha separadora
    pr.separador(120, caracter='-')  # Imprimimos uma linha separadora
    # Imprimimos o subtotal da compra
    pr.imprimir('Total', tamanho=107, alinhar='fim', end='|')  # Imprimimos o subtotal da compra
    pr.imprimir('R$', str(round(total_compra, 2)), tamanho=12, alinhar='fim')  # Imprimimos o valor do subtotal
    # Imprimimos o total a pagar
    pr.imprimir('Total a pagar', tamanho=107, alinhar='fim', end='|')  # Imprimimos o total a pagar
    pr.imprimir('R$', str(round(total, 2)), tamanho=12, alinhar='fim', cor_texto='verde negrito')  # Imprimimos o valor do total a pagar com texto verde e negrito
    # Limpamos a formatação do texto
    pr.limpar_formatacao()  # Limpamos a formatação do texto
    # Pulamos duas linhas
    pr.pular_linha()  # Pulamos uma linha
    pr.pular_linha()  # Pulamos outra linha

# Esta função mostra os produtos que você adicionou à sua compra.
def imprime_compra(compra):  # Esta função recebe a compra como entrada
    # Se houver produtos na lista de compra
    if len(compra) > 0:  # Se a lista de produtos não estiver vazia
        # Inicializamos a variável 'total' para guardar o subtotal da compra
        total = 0
        # Imprimimos o cabeçalho da tabela de produtos da compra
        pr.imprimir('codigo', tamanho=6, alinhar='centro', end='|')  # Imprimimos a coluna 'codigo'
        pr.imprimir('produto', tamanho=83, alinhar='centro', end='|')  # Imprimimos a coluna 'produto'
        pr.imprimir('qtd', tamanho=3, alinhar='centro', end='|')  # Imprimimos a coluna 'qtd' (quantidade)
        pr.imprimir('valor un.', tamanho=12, alinhar='centro', end='|')  # Imprimimos a coluna 'valor un.' (valor unitário)
        pr.imprimir('valor', tamanho=12, alinhar='centro')  # Imprimimos a coluna 'valor' (valor total)
        # Percorremos a lista de produtos da compra, um por um
        for produto in compra:  # Para cada produto na lista de produtos
            # Imprimimos as informações do produto
            imprimir_produto(produto)  # Chamamos a função 'imprimir_produto' para imprimir as informações do produto
            # Calculamos o valor total do produto
            total += produto['valor'] * produto['quantidade']  # Somamos o valor total do produto ao subtotal da compra
        # Imprimimos uma linha separadora
        pr.separador(120, caracter='-')  # Imprimimos uma linha separadora
        # Imprimimos o subtotal da compra
        pr.imprimir('Subtotal', tamanho=107, alinhar='fim', end='|')  # Imprimimos o subtotal da compra
        pr.imprimir('R$', str(round(total, 2)), tamanho=12, alinhar='fim')  # Imprimimos o valor do subtotal
    # Caso contrário (se a lista de produtos estiver vazia)
    else:
        # Imprimimos uma mensagem informando que a lista está vazia
        pr.imprimir('Sem itens na lista ainda', tamanho=120, alinhar='center')  # Imprimimos a mensagem de lista vazia
    # Pulamos duas linhas
    pr.pular_linha()  # Pulamos uma linha
    pr.pular_linha()  # Pulamos outra linha

# Esta função imprime as informações de um produto, como código, nome, quantidade e valor.
def imprimir_produto(produto):  # Esta função recebe o produto como entrada
    # Imprimimos o código do produto
    pr.imprimir(str(produto['codigo']), tamanho=6, alinhar='fim', caracter='0', end='|')  # Imprimimos o código do produto
    # Imprimimos o nome do produto
    pr.imprimir(produto['nome'], tamanho=83, caracter='.', end='|')  # Imprimimos o nome do produto
    # Imprimimos a quantidade do produto
    pr.imprimir(str(produto['quantidade']), tamanho=3, caracter='0', alinhar='fim', end='|')  # Imprimimos a quantidade do produto
    # Imprimimos o valor unitário do produto
    pr.imprimir('R$', str(round(produto['valor'], 2)), tamanho=12, alinhar='fim', end='|')  # Imprimimos o valor unitário do produto
    # Imprimimos o valor total do produto
    pr.imprimir('R$', str(round(produto['valor'] * produto['quantidade'], 2)), tamanho=12, alinhar='fim')  # Imprimimos o valor total do produto

# Esta função imprime o cabeçalho do nosso sistema de vendas.
def imprimir_cabecalho(erro):  # Esta função recebe a mensagem de erro como entrada
    # Limpamos a tela
    pr.limpar()  # Limpamos a tela
    # Imprimimos o cabeçalho do sistema
    pr.retangulo('{reprograma}\nProjeto Guiado 1\nTerminal de Vendas', sv=1, tamanho=100, margem=10, cor_texto='azul negrito', cor_barra='magenta')  # Imprimimos o cabeçalho com texto azul negrito e barra magenta
    # Imprimimos uma linha separadora
    pr.separador(120, cor_texto='ciano')  # Imprimimos uma linha separadora com cor ciano
    # Se houver uma mensagem de erro
    if erro != '':  # Se a mensagem de erro não estiver vazia
        # Imprimimos a mensagem de erro
        pr.imprimir(erro, tamanho=120, alinhar='centro', cor_texto='vermelho negrito')  # Imprimimos a mensagem de erro com texto vermelho negrito
        # Imprimimos uma linha separadora
        pr.separador(120, cor_texto='ciano')  # Imprimimos uma linha separadora com cor ciano
    # Setamos a mensagem de erro como vazia
    erro = ''

# Esta função mostra as opções de ajuda do sistema.
def imprimir_ajuda():  # Esta função não recebe nenhuma entrada
    # Pulamos duas linhas
    pr.pular_linha(quantidade=2)  # Pulamos duas linhas
    # Imprimimos as opções de ajuda
    pr.imprimir('[H]   >> Ajuda com o Sistema', alinhar='centro', tamanho=120)  # Imprimimos a opção de ajuda '[H]'
    pr.imprimir('[Q]   >> Sair da Tela ou Sistema', alinhar='centro', tamanho=120)  # Imprimimos a opção de ajuda '[Q]'
    pr.imprimir('[N]   >> Cria uma Nova Compra', alinhar='centro', tamanho=120)  # Imprimimos a opção de ajuda '[N]'
    pr.imprimir('[F]   >> Fechar a Compra', alinhar='centro', tamanho=120)  # Imprimimos a opção de ajuda '[F]'
    pr.imprimir('[P]   >> Confirmar que a compra foi paga', alinhar='centro', tamanho=120)  # Imprimimos a opção de ajuda '[P]'
    pr.imprimir('[nnn] >> Adicionar o codigo do produto a compra', alinhar='centro', tamanho=120)  # Imprimimos a opção de ajuda '[nnn]'
    pr.imprimir('[Xnn] >> Muda a quantidade de itens adicionado', alinhar='centro', tamanho=120)  # Imprimimos a opção de ajuda '[Xnn]'
    pr.imprimir('[E]   >> Encerar caixa', alinhar='centro', tamanho=120)  # Imprimimos a opção de ajuda '[E]'
    # Pulamos duas linhas
    pr.pular_linha(quantidade=2)  # Pulamos duas linhas

# Esta função imprime o rodapé do sistema, com as opções de ajuda e sair.
def imprimir_rodape():  # Esta função não recebe nenhuma entrada
    # Imprimimos as opções do rodapé
    pr.imprimir('[H] Ajuda ', '[Q] Sair ', caracter='═', tamanho=115, alinhar='fim', end='╣')  # Imprimimos as opções de ajuda e sair no rodapé
    # Lê a opção do usuário
    return input().lower()  # Lê a opção do usuário e converte para letras minúsculas

# Esta é a função principal do nosso programa, onde o menu de vendas é exibido.
def menu():  # Esta função não recebe nenhuma entrada
    # Inicializamos as variáveis
    opcao = ''  # Inicializamos a variável 'opcao' como uma string vazia
    erro = ''  # Inicializamos a variável 'erro' como uma string vazia
    tela = ''  # Inicializamos a variável 'tela' como uma string vazia
    compra = []  # Inicializamos a variável 'compra' como uma lista vazia (para armazenar os produtos da compra atual)
    compras = []  # Inicializamos a variável 'compras' como uma lista vazia (para armazenar as compras fechadas)
    # Loop principal do menu
    while opcao != 'q':  # Enquanto a opção do usuário for diferente de 'q' (sair)
        # Imprimimos o cabeçalho do sistema
        imprimir_cabecalho(erro)  # Chamamos a função 'imprimir_cabecalho' para imprimir o cabeçalho
        # Verificamos a tela atual
        if tela == '':  # Se a tela atual for vazia (tela inicial)
            pr.pular_linha(quantidade=4)  # Pulamos 4 linhas
        elif tela == 'ajuda':  # Se a tela atual for a tela de ajuda
            imprimir_ajuda()  # Chamamos a função 'imprimir_ajuda' para imprimir as opções de ajuda
            tela = ''  # Definimos a tela atual como vazia (retorna para a tela inicial)
        elif tela == 'compra':  # Se a tela atual for a tela de compra
            imprime_compra(compra)  # Chamamos a função 'imprime_compra' para imprimir a lista de produtos da compra atual
        elif tela == 'fechar':  # Se a tela atual for a tela de fechar a compra
            imprime_compra_fechada(compra, total)  # Chamamos a função 'imprime_compra_fechada' para imprimir a compra fechada
        elif tela == 'encerar':  # Se a tela atual for a tela de encerrar o caixa
            imprime_fechamento_caixa(compras)  # Chamamos a função 'imprime_fechamento_caixa' para imprimir o fechamento do caixa
            compras = []  # Limpamos a lista de compras fechadas
            tela = ''  # Definimos a tela atual como vazia (retorna para a tela inicial)
            pr.pular_linha(quantidade=2)  # Pulamos 2 linhas
        # Lê a opção do usuário
        opcao = imprimir_rodape()  # Chamamos a função 'imprimir_rodape' para imprimir as opções do rodapé e ler a opção do usuário
        # Processamos a opção do usuário
        if opcao == 'h':  # Se a opção do usuário for 'h' (ajuda)
            tela = 'ajuda'  # Definimos a tela atual como 'ajuda'
        elif opcao == 'n':  # Se a opção do usuário for 'n' (nova compra)
            tela = 'compra'  # Definimos a tela atual como 'compra'
        elif opcao == 'f':  # Se a opção do usuário for 'f' (fechar compra)
            total = calcula_total_desconto(compra)  # Chamamos a função 'calcula_total_desconto' para calcular o total da compra
            tela = 'fechar'  # Definimos a tela atual como 'fechar'
        elif opcao == 'e':  # Se a opção do usuário for 'e' (encerrar caixa)
            tela = 'encerar'  # Definimos a tela atual como 'encerar'
        elif 'p' in opcao:  # Se a opção do usuário contiver 'p' (pagar)
            compras.append({'itens': compra, 'total': total, 'data': datetime.now()})  # Adiciona a compra atual à lista de compras fechadas
            compra = []  # Limpamos a lista de produtos da compra atual
            tela = ''  # Definimos a tela atual como vazia (retorna para a tela inicial)
        else:  # Caso contrário (opção inválida)
            try:  # Tentamos converter a opção do usuário para um número inteiro
                codigo = int(opcao)  # Converte a opção para um número inteiro
                produto = produto_codigo(codigo)  # Chamamos a função 'produto_codigo' para encontrar o produto com o código fornecido
                compra.append(novo_produto(produto, 1))  # Adiciona o produto à lista de produtos da compra atual
            except ValueError:  # Se a opção do usuário não for um número inteiro
                erro = 'A opção selecionada não existe no sistema'  # Definimos a mensagem de erro
            except TypeError:  # Se o produto não for encontrado
                erro = 'O código do produto não existe' # Define a mensagem de erro

# Esta função calcula o total da compra, aplicando um desconto se necessário.
def calcula_total_desconto(compra):  # Esta função recebe a compra como entrada
    # Inicializamos a variável 'total'
    total = 0
    # Percorremos a lista de produtos
    for produto in compra:  # Para cada produto na lista de produtos
        # Calculamos o valor total do produto
        total += (produto['valor'] * produto['quantidade'])  # Somamos o valor total do produto ao total da compra
    # Aplicamos a regra de desconto (implemente aqui a lógica para aplicar desconto)
    # ...
    # Retornamos o total da compra com desconto
    return total

# Chamamos a função 'menu' para iniciar o programa
menu()
