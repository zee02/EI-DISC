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
        return z
    
#ex5
def soma_Fib(n):
    soma=0
    for i in range(1,n+1):
        soma+=F(i)
    return soma
soma_Fib(6)
