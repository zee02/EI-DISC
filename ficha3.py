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
U=A|B|C # U=A.union(B.union(C))
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