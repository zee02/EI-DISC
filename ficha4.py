# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 09:38:02 2022

@author: zclpa
"""

import matplotlib.pyplot as plt
import math as mt

# %% Exercicio 1 a)

print("São necessários", str(mt.ceil(100 / 8)), "bytes")

# b)


def conversor(x):
    print("São necessários", str(mt.ceil(x / 8)), "bytes")


conversor(100)


# %% Exercicio 2


def inteiro(x):
    if x >= 0:
        print("A parte inteiro do número real " + str(x) + " é " + str(mt.floor(x)))
    else:
        print("A parte inteiro do número real " + str(x) + " é " + str(mt.ceil(x)))


inteiro(-3.6)

# %% Exercicio 3


def bissexto(x):
    if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
        print("É ano bissexto")
    else:
        print("Não é ano bissexto")


bissexto(2015)


# %% Exercicio 4


def F(n):
    if n == 1 or n == 2:
        return 1
    elif n >= 3:
        return F(n - 1) + F(n - 2)
    else:
        print("Insira um número positivo")


# % Exercicio 5


def Fib(n):
    soma = 0
    for i in range(1, n + 1):
        soma += F(i)
    return soma


Y = Fib(6)
print(Y)


# %% Exercicio 4 - Alternativo sem função


# def F(n):
#    if n == 1 or n == 2:
#        return 1
#    else:
#        x = 1
#        y = 1
#        for i in range(3, n + 1):
#            z = x + y
#            x = y
#            y = z
#            return z


# print(F(6))


# %% Exercicio 7


nouro = (1 + mt.sqrt(5)) / 2

n = 2
Q = 1


def F(n):
    if n == 1 or n == 2:
        return 1
    elif n >= 3:
        return F(n - 1) + F(n - 2)
    else:
        print("Insira um número positivo")


while abs(Q - nouro) > 10 ** -10:
    n += 1
    Q = F(n) / F(n - 1)
    plt.plot(n, Q, "*r")
print("O valor aproximado é ", Q)


# %% Exercicio 9

# a cong mod m b se a%m = b%m

# d%7 = (50+A+(seculo-1)//4 + A //4-2*(seculo-1))%7
# como d=0,1,2..6 d%7=d
# d = (50+A+(seculo-1)//4 + A //4-2*(seculo-1))%7


def Natal(ano):
    A = ano % 100  # se ano fr str '2017' int(ano[2:3])
    seculo = mt.ceil(ano / 100)
    d = (50+A+(seculo-1)//4 + A // 4-2*(seculo-1)) % 7
    DIAS = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']
    print(f'No ano {ano} o Natal é à/ao {DIAS[d]}')


Natal(2017)
Natal(2032)
Natal(2050)


# %% Exercicio 10
ns = input("Insira o nº de série da nota: ")
letra = ns[0]
numeros = ns[1: len(ns)]

soma = 0

for i in range(0, len(numeros)):
    soma += int(numeros[i])
letras = ["R", "S", "T", "U", "M", "N"]
Beta = letras.index(letra)

soma += Beta  # beta+x1+x2+...+x10+d
# a soma e o 0 são congruentes modulo 0, ou seja % 9 == 0 % 9
# logo a soma tem de ser multiplo de 9

if soma % 9 == 0:
    print("A nota é válida")
else:
    print("A nota não é válida")


# %% Exercicio 11 a)

def Identificador():
    n = input('Insira o número de estudante: ')
    campus = int(n[0])
    ano = int(n[1:3])
    # d4+d5+d6+d7%5 = D%5 = D
    soma = 0
    for i in range(3, len(n)):
        soma += int(n[i])

    D = soma % 5
    DIAS = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']

    print(f'Campus {campus} - Ano letivo {ano}/{ano+1} - {DIAS[D]}-feira')


Identificador()

# %% Exercicio 12 a)

#CC = input('Insira o número do cartão de crédito: ')
# 5027811020103X

# 1047712040206X

#34 + X

# para ser multiplo de 10 X tem de ser 6


# %% Exercicio 12 b)
# 4012888888881882


def validar():
    CC = input('Insira o número de cartão de crédito: ')
    CClist = list(CC)
    for i in range(0, len(CC)):
        CClist[i] = int(CClist[i])
    CClist.reverse()
    # ou sem usar o comando reverse podemos usar um for e uma variável auxiliar
    # aux=list()
    # for i in range(0,len(CC)):
    #    aux[i]=CClist[len(CC)-1-i]
    for i in range(1, len(CC), 2):  # range(inicio,limite,step)
        X = CClist[i]
        if 2*X > 9:
            X = int(2*X/10)+(2*X) % 10  # ou X=2*X; X=str(X) ;X=int(X[0])+int(X[1])
        else:
            X = 2*X
        CClist[i] = X
    soma = 0
    for i in range(0, len(CC)):
        soma += CClist[i]
    if soma % 10 == 0:  # soma tem de ser congruente com 0 modulo 10
        # soma%10=0%10=0
        print('O Cartão de crédito é válido')
    else:
        print('O Cartão de crédito é inválido')


validar()
# Insira o número de cartão de crédito: 378282246310004
# O Cartão de crédito é inválido
# Insira o número de cartão de crédito: 371449635398431
# O Cartão de crédito é válido
