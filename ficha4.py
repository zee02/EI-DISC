#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 09:57:02 2022

@author: zeeee
"""

#Ficha 4
#ex1a)
import math
print("São necessários", +str(math.ceil(100/8)) + 'bytes' )

#ex1b)
def conversor(x):
    print("São necessários", +str(math.ceil(x/8))+ 'bytes')
    


#ex2
def inteiro(x):
    if x>=0:
        return math.floor(x)
    else:
        return math.ceil(x)
    
#ex3
#op1 fazendo Leitura do enunciado
def bissexto(x):
    if x%4==0:
        if x%100==0 and x%400!=0:
            print("Não é bissexto")
        else:
            print("é bissexto")
    else:
        print("não é bissexto")
        
#ou
def Bissexto(x):
    if x%4==0 or x%100==0 and x%500!=0:
            print("Não é bissexto")
    else:
        print("é bissexto")

#ex4
#op1 recursiva chamando a si propria
def F(n):
    if n==1 or n==2:
        return 1
    elif n>=3:
        return F(n-1)+F(n-2)
    else:
        print("Insira um inteiro positivo")
        
F(6)

#op2 definir F(n) sem chamar a si propria
def F(n):
    if n==1 or n==2:
        return 1
    else:
        x=1
        y=1
        for i in range(3,n+1):
            z=x+y
            x=y
            y=z
        return z
    
#ex5
def soma_Fib(n):
    soma=0
    for i in range(1,n+1):
        soma+=F(i)
    return soma
soma_Fib(6)

#ex7
import math
nouro=(1+math.sqrt(5))/2
n=2
Q=1
while abs(Q-nouro)>10**-10:
    n+=1
    Q=F(n)/F(n-1)
print("O valor aproximado obtido é: ", Q)
#ou
print(f'O valor aproximado solicitado é (Q) e é atingido quando n={n}')

#b) representação gráfica
import  matplotlib.pyplot as plt

nouro=(1+math.sqrt(5))/2
n=2
Q=1
X=[2] #iniciar a lista dos objetos começando por n=2
#como array X=np.array([2])
Y=[1] #iniciar a lista das imagins com a primeira
###
while abs(Q-nouro)>10**-10:
    n+=1
    Q=F(n)/F(n-1)
    X.append(n)
    Y.append(Q)
    ###
plt.plot(X,Y,'*')

#ex10

ns=input("Insira o número de serie da nota: ")
letra=ns[0]
numeros=ns[1:len(ns)]
soma=0
for i in range(0,len(numeros)):
    soma+=int(numeros[i])
letras=['R','S','T', 'U', 'M', 'N']
Beta=letras.index(letra)

soma+=Beta # beta+x1+x2+..+x10+d
#a soma e o 0 são congruentes ao modulo 9
#ou seja soma%9==0%9 logo soma tem de ser multiplo de 9

if soma%9==0:
    print("A nota é válida!")
else:
    print("A nota não é válida!")
    
#aula8
#1A)
import numpy as np
MR=np.array([[1,0,1,0], [1,0,1,0], [1,1,0,0], [0,0,0,1]])
print(MR)


#1B) A relação inversa de R^-1{(aj,ai) | (ai,aj) in R}
MRinv=MR.T
print("A matriz da relação inversa é: ", MRinv)

#1C)
MR2 = MR@MR

def um(M):
    [l,c] = M.shape
    for i in range(0,l):
        for j in range(0,c):
            if M[i,j]!=0:
                M[i,j] = 1
    return M
MR2=um(MR2)
print("A matriz da relação R^2 é: ", MR2)

#ou
MR2 = MR@MR
MR2[MR2!=0]=1


MR3=MR2@MR
MR3[MR3!=0]=1
print("A matriz da relação R^3 é: ", MR3)

#1D)
print("A relação R não é reflexiva porque existem entradas nulas na diagonal principal")
print("R não é simétrica porque, por ex, (2,1) in R mas (1,2) not in R")
print("Não é antissimétrica porque (1,3) in R e (3,1) in R mas 1 não é igual a 3")

#1E)
#fecho reflexivo
MRefR= MR + np.eye(4)
MRefR=um(MRefR)

#ex4
def is_reflexiva(M):
    [l,c]=M.shape
    contador=0
    for i in range(0,l):
        contador+=1
    if contador!=l:
        return False
    else:
        return True
    
#ou 

def is_reflexiva(M):
    [l,c]=M.shape
    for i in range(0,l):
        if M[i,i] == 0:
            return False
    return True

#ex4B)

def is_simetrica(M):
    [l,c]=M.shape
    for i in range(0,l):
        for j in range(i+1,c):
            if M[i,j]!=M[j,i]:
                return False
        return True
#ou
def is_simetrica(M):
    return np.array_equal(M,M.T)

#ou
def is_simetrica(M):
    return (M==M.T).all()

#ex4C)

def is_transitiva(M):
    A=M+M@M
    A[A!=0]=1
    return (M==A).all()

#ou calculando o fecho transitivo e comparando com MR

def is_transitiva(M):
    [l,c]=M.shape
    A=M #A será a matriz do fecho transitivo
    for i in range(2,l+1):
        A=A+np.linalg.matrix_power(MR,i)
    A[A!=0]=1
    return (M==A).all()
