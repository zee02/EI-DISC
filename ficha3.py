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
A=set()
for i in range(1, 411):
    if i%2==0 & i%7!=0:
        A.add(i)
print(len(A))

#b
QP=set()
for i in range(1, 21):
    QP.add(i**2)
print(QP)
    
#c
M3=set(range(3,411,3)) #multiplos de 3
C=M3-QP
print(C)

#ex7
L1 = ["Futebol", "Ioga", "Cinema", "Futebol", "Concertos", "Cinema", "Concertos"]

#ex8
B={1,2,3,4}
P=[{1},{2},{3,4}]
if P[0]|P[1]|P[2]==B:
    if P[0]&P[1]==set() and P[0]&P[2]==set() and P[0]&P[3]==set():
        print("É partição de B")
    else:
        print("Não é partição porque a interseção ")
else:
    print("Não é partição porque a união não deu B")


#ex9
def Particao(P):
    I=set()
    for i in range(0, len(P)):
        for j in range(i+1, len(P)):
            I= I|(P[i]&P[j])
    if I!=set():
        print("Não é partição")
    else:
        U=set()
        for A in P:
            U=U|A
        print("É partição do conjunto ", U)    
P=[{5}, {2}, {3,4}]
Particao(P)

def particao(P):
    i = set()
    for i in range(0, len(P)):
        for j in range(i+1, len(P)):
            if P[i]&P[j]!=set():
                print("Não é partição")
                return
    U=set()
    for A in P:
        U=U|A
    print("É partição do conjunto " ,U)
particao(P)
            
    














