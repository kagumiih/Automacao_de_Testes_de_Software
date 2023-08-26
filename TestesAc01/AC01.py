import pytest
from funcoes import calcular_desconto
from funcoes import calcular_salario_lqd
from funcoes import calcular_conta_gorjeta


#Exercício 01

#Faça uma função que efetua o cálculo do salário líquido de um professor. Os dados fornecidos serão: valor hora aula, número de aulas dadas e o percentual de desconto do INSS.

def test_calculo_salario_lqd():
    valor_hora_aula = 6.25
    numero_aulas = 160
    percentual_desconto_inss = 1.3

    salario_liquido = calcular_salario_lqd(valor_hora_aula, numero_aulas, percentual_desconto_inss)
    assert salario_liquido == 987.00  

def test_calculo_salario_lqd_sem_desconto_inss():
    valor_hora_aula = 20.5
    numero_aulas = 240
    percentual_desconto_inss = 1.7  

    salario_liquido = calcular_salario_lqd(valor_hora_aula, numero_aulas, percentual_desconto_inss)
    assert salario_liquido == 4836.36  

def test_calculo_salario_lqd_com_desconto_maximo_inss():
    valor_hora_aula = 13.9
    numero_aulas = 200
    percentual_desconto_inss = 6.48  

    salario_liquido = calcular_salario_lqd(valor_hora_aula, numero_aulas, percentual_desconto_inss)
    assert salario_liquido == 2599.86


#Exercício 02

#Em épocas de pouco dinheiro, os comerciantes estão procurando aumentar suas vendas oferecendo desconto aos clientes. 
# Faça uma função que receba um valor de um produto e devolva um novo valor tendo em vista que o desconto foi de 9%.

def test_desconto_equivale_nove_porcento():
    valor_produto1 = 100
    valor_desconto1 = calcular_desconto(valor_produto1)
    assert valor_desconto1 == 91.00
    assert valor_produto1 - valor_desconto1 == 9.00

    valor_produto2 = 1500
    valor_desconto2 = calcular_desconto(valor_produto2)
    assert valor_desconto2 == 1365.00
    assert valor_produto2 - valor_desconto2 == 135.00

    valor_produto3 = 60000
    valor_desconto3 = calcular_desconto(valor_produto3)
    assert valor_desconto3 == 54600.00
    assert valor_produto3 - valor_desconto3 == 5400.00


#Exercício 03

#Faça uma função que leia dois números reais, um será o valor de um produto e o outro o valor do desconto que esse produto está recebendo. 
# Devolva quantos reais o produto custa na promoção.


def test_desconto_50():
    assert calcular_desconto(500, 50) == 450


def test_desconto_10500():
    assert calcular_desconto(10500, 500) == 10000


def test_desconto_90():
    assert calcular_desconto(90, 0.80) == 89.20


#Exercício 04

#Todo restaurante, embora por lei não possa obrigar o cliente a pagar, cobra 10% de comissão para o garçom. 
# Faça uma função que receba o valor gasto com despesas realizadas em um restaurante e devolva o valor total da conta e o valor da gorjeta.

def test_calculo_valor_total_conta():
    valor_despesas = 75.00    

    valor_total, gorjeta = calcular_conta_gorjeta(valor_despesas)
    assert valor_total == 82.50 
    assert gorjeta == 7.5  

def test_calculo_valor_total_conta_2():
    valor_despesas = 125  
    valor_total, gorjeta = calcular_conta_gorjeta(valor_despesas)
    assert valor_total == 137.50  
    assert gorjeta == 12.5  

def test_calculo_valor_total_conta_sem_despesas():
    valor_despesas = 350.87  
    valor_total, gorjeta = calcular_conta_gorjeta(valor_despesas)
    assert valor_total == 385.96  
    assert gorjeta == 35.09

#-----------------------------#

#Juliane Teixeira Cobiank RA:2102159