import sys
sys.stdin = open('maxdist.in')
sys.stdout = open('maxdist.out','w')

n = int(input())
p = [] 
for i in range(n):
     x,y = map(int,input().split())
     p.append((x,y))
    
m = int(input())        
Inf = 10**10
d = [[Inf]*n for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    x1,y1 = p[a]
    x2,y2 = p[b]
    dist = ((x1-x2)**2+(y1-y2)**2)**0.5
    d[a][b] = min(dist, d[a][b])
    d[b][a] = min(dist, d[b][a])   
for i in range(n):
    d[i][i] = 0    

for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])
      
m = max(map(max, d))
print('-1' if m == Inf else m)