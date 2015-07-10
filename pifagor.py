import sys
import math

sys.stdin = open('pifagor.in')
sys.stdout = open('pifagor.out', 'w')

l = [int(x) for x in input().split()]
n = len(l)
assert n == 9
# Сортируем по убыванию
l = sorted(l, reverse=True)

for i in range(n-3):
    for j in range(i+1, n-2):
        for k in range(j+1, n):            
           A,B,C = l[i], l[j], l[k]
           for i1 in range(i+1, n):
                if i1 == j or i1 == k: continue                
                for j1 in range(i1+1, n-3):
                    if j1 == j or j1 == k: continue
                    a, b = l[i1], l[j1]
                    if A*b != B*a: continue                   
                    for k1 in range(j1+1, n-2):
                        if k1 == j or k1 == k: continue                       
                        c = l[k1] 
                        if A*c != C*a: continue 
                        print(A, B, C) 
                        print(a, b, c) 
                        sys.exit()