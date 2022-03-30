#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 09:55:39 2022

@author: zeeee
"""

A={1,2,3,4}
B={3,4,5,6,7}
C={1,5,9,10}

#a
U=A|B|C # U=A.union(B.union(C)) União de conjuntos
print(U)

#b
print(len(U))

#c
Ac=U-A
print(Ac)

#d
A_B=A-B
print(A_B)

#e
AdsB = A^B #diferença simétrica

#ex2

#ex3

def simdiff(A,B):
    return (A-B) | (B-A)  # ou (A|B) -(A&B)

#ex5
#a)
B=set(range(70,141,7))
#ou
B=set()
for i in range(66, 141):
    if i%7==0:
        B.add(i)
#ou
B={x for x in range(66,141) if x%7==0}

#b)
A=set(range(3,101,3))
C=A^B
print(len((A|C)&B))

#ex6
#a
#teoria de conjuntos e operações de conjuntos
P=set(range(2,411,2)) #pares
M7=set(range(7,411,7)) #multiplos de 7
A=P-M7
print(len(A))

#b
for i in range(1, 410):

















