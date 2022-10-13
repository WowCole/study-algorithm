t = int(input())
for a in range(t):
    i,j=input().split()
    print(j[:int(i)-1] +j[int(i):])