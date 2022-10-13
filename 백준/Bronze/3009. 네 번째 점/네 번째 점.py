x=[]
y=[]
for i in range(3):
    a,b=map(int,input().split())
    x.append(a)
    y.append(b)


for j in range(3):
    if x.count(x[j])==1:
        nx=x[j]
    if y.count(y[j])==1:
        ny=y[j]

print(nx,ny)