x = [2,1,7,8,3,4,2,3]
y = [3,1,7,2,5,6,1,1]
k=2


def f(a,b,x,y):
    return  round((abs(a-x)**2 + abs(b-y)**2  )**(0.5),2)    

n = len(x)
data = [ [0]*n for _ in range(k) ]

g = [ [0]*n for _ in range(k)]
old_g = [ [0]*n for _ in range(k)]

#c = [(3,9.5), (6.5,5.25), (1.5,3.5)]
c = [(2,3), (1,1)]
while True:
    for j in range(k):
        for i in range(n):
            data[j][i] = f(c[j][0],c[j][1],x[i],y[i])

    for i in range(k):
        for j in range(n):
            g[i][j]= 1 if data[i][j]==min([ data[temp][j] for temp in range(k)]) else 0

    for i in range(k):
        cx=cy=0
        for j in range(n):
            cx += round( (x[j]*g[i][j])/sum([ g[i][temp] for temp in range(n) ]) ,2)
            cy += round( (y[j]*g[i][j])/sum([ g[i][temp] for temp in range(n) ]) ,2)
        c[i]=(cx,cy)

    print('***************************')    
    for row in data:
        print(*row)
    print()
    
    for row in g:
        print(*row)
    print(c)

    if old_g==g:
        break

    print()
    for i in range(k):
        for j in range(n):
            old_g[i][j] = g[i][j]

print()
for i in range(k):
    print('Cluster '+str(i+1)+' : ',end=' ')
    for j in range(n):
        if g[i][j]==1:
            print(j+1,end=' ')
    print()

