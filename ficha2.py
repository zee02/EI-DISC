#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 08:48:20 2022

@author: zeeee
"""
import math
import numpy as np
import matplotlib.pyplot as plt

#ex.2 a)

def f(x):
    y=math.cos(x)+math.exp(x)
    return y

#b)
print("A imagem de f de 0 é: ", f(0))
print("A imagem de f de pi é: ",f(math.pi))


#c
X=np.linspace(1,2,98)

#d
# inicialmente falhou f(X) porque não está à espera de receber um vetor 

def f(x):
    return np.cos(x)+np.exp(x)
f(X)


#e

Y=f(X)
plt.plot(X,Y)

#ex.3
def F(x):
    return x**5-3*x**4-3*x**3+7*x**2+6*x
    
X=np.arange(-1.5,2.51,0.125)
Y=F(X)
plt.plot(X,Y)

#ex4

def r(t):
    C = float(input("Insira a quantidade de polónio: "))
    v = float(input("Insira o tempo de meia vida: "))
    return C*(0.5)**(t/v)

r(10)

#a forma anterior não é prática se quisermos calcular
#imagens de um vetor
#irá solicitar constantemnente os inputs

def r(t):
    return 10*(0.5)**(t/140)

T=np.arange(7,70.1,7)
Y = r(T)
#a quantidade de polonio ao final de cada semana é dada pelas entradas do vetor Y
print(Y)

#alternative à resposta da 1ª questão
for i in T:
    print(f'No dia {i} a quantidade de polónio é {r(i)}')

#2ª questão
T=np.arange(7,70.1,7)
Y = r(T)
plt.plot(T,Y,"o")

#ex.5
#a

plt.plot()

def Z(n):
    soma=0
    for k in range(1,n+1):
        soma+=(0.5)**k
    return soma

#aula 4 ---------
import numpy as np
N=np.arange(1,21)
#não é possível definir Y=Z(N) porque 
#a função Z espera como input um escalar(não um vetor)

Y=np.array([])
for k in N:
    Y=np.append(Y,Z(k))

import matplotlib.pyplot as plt
plt.plot(N,Y,'o')

n=2
while abs(Z(n)-Z(n-1))>=10**(-10):
    n+=1
print(n)


#ex6

nota_PE1 = float(input("Insira a nota da 1ª prova escrita: "))
nota_PE2 = float(input("Insira a nota da 2ª prova escrita: "))
nota_TP1 = float(input("Insira a nota da 1º teste prático: "))
nota_TP2 = float(input("Insira a nota da 2º teste prático: "))
if nota_PE2<8.0 or nota_TP2<8.0:
    print("Não atingiu o mínimo numa das componentes.")
else:
    nota_CT=max(0.3*nota_PE1+0.7*nota_PE2, nota_PE2)
    nota_CP=max(0.3*nota_TP1+0.7*nota_TP2, nota_TP2)
    print("A classificação final na UC é ", 0.4*nota_CP+0.6*nota_CT)
    
    
#-----ficha 3------
