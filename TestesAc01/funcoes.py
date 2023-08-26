import pytest

def calcular_salario_lqd(valor_hora_aula, numero_aulas, percentual_desconto_inss):
    salario_bruto = valor_hora_aula * numero_aulas
    desconto_inss = (salario_bruto * percentual_desconto_inss) / 100
    salario_liquido = salario_bruto - desconto_inss
    return round(salario_liquido, 2)

#------------------------------#

def calcular_desconto(valor_produto):
    return valor_produto * 0.91

#------------------------------#

def calcular_conta_gorjeta(valor_despesas):
    # Calcula o valor da gorjeta (10% do valor das despesas)
    gorjeta = 0.1 * valor_despesas
    
    # Calcula o valor total da conta (valor das despesas + gorjeta)
    valor_total_conta = valor_despesas + gorjeta
    
    return valor_total_conta, gorjeta

# Solicita o valor gasto com despesas ao usuário
valor_despesas = float(input("Digite o valor gasto com despesas: R$"))

# Chama a função para calcular a conta e a gorjeta
total_conta, valor_gorjeta = calcular_conta_gorjeta(valor_despesas)

# Exibe os resultados
print(f"Valor total: R${total_conta:.2f}")
print(f"Valor da gorjeta: R${valor_gorjeta:.2f}")
def calcula_desconto(valor_produto):
    return valor_produto * 0.91






