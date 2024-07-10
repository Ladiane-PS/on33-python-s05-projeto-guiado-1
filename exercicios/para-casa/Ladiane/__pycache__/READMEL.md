# Promoções Inspiradoras (Básico)

## Descrição

Esta função calcula o valor total da compra aplicando descontos especiais conforme as promoções oferecidas pela loja.

### Promoções:

1. **Desconto para compras acima de R$ 100:**
   - Clientes que gastam mais de R$ 100 recebem um desconto de 10% no valor total da compra.

2. **Desconto para combos:**
   - Se o cliente comprar mais de um item do mesmo tipo, recebe um desconto de 50% a partir do segundo item.

### Implementação da Função

:rocket: **Demonstração da função em ação**

```python
def calcula_total_desconto(compra):
    """
    Calcula o valor total da compra aplicando os descontos conforme as promoções.
    
    Parâmetros:
    compra (list): Lista de dicionários contendo os itens da compra, 
                   onde cada dicionário possui 'codigo', 'quantidade' e 'valor'.
    
    Retorna:
    float: Valor total da compra com os descontos aplicados.
    """
    total = 0  # Inicializa o valor total da compra
    itens_por_codigo = {}  # Dicionário para contar a quantidade de cada produto

    for produto in compra:
        codigo = produto['codigo']
        quantidade = produto['quantidade']
        valor = produto['valor']
        
        if codigo not in itens_por_codigo:
            itens_por_codigo[codigo] = 0
        
        itens_por_codigo[codigo] += quantidade

        if itens_por_codigo[codigo] > 1:
            total += valor * 0.5 * quantidade  # Aplica 50% de desconto a partir do segundo item
        else:
            total += valor * quantidade
    
    if total > 100:
        total *= 0.9  # Aplica desconto de 10% se o total for maior que R$ 100

    return total