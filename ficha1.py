#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 09:00:33 2022

@author: zeeee
"""

import numpy as np
import math


#ex.1

A = np.array([[2,1,-1],[-1,2,1],[1,3,-3]])
B = np.array([[3],[-1],[0]])
C = np.array([[1,0,-2,2],[0,2,3,0],[1,0,-1,0]])
D = np.array([[1,-1,0,2]])

#ex.1 a)

#i) AB
resultado = A @ B
print(resultado)

#ii) CD
#esultado = C @ D
print(resultado)

#iii) C * D transposta
resultado = C @ (D.T)
print(resultado)

#iv) A * B transposta
resultado = A @ (B.T)
print(resultado)

#v) A inversa * C
resultado = np.linalg.inv(A) @ C
print(resultado)

#vi) 3AB + 2C * D transposta
resultado = (3*A@B) + (2*C @ (D.T))
print(resultado)

#vii) elemento ao quadrado
resultado = A**2
print(resultado)

#viii) A ao quadrado
resultado = A@A
print(resultado)

#ix) det(a * A transposta)
resultado = np.linalg.det(A @ (A.T))
print(resultado) 

#x) B * D * C transposta
resultado = (B @ D) @ (C.T)
print(resultado)

#xi) B ao quadrado
resultado = B @ B
print(resultado)

#xii) A ao quadrado * b transposta
resultado = (A@A) @ (B.T)
print(resultado)



#ex.1 b)

C[:,2:3]