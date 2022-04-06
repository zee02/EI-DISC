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
