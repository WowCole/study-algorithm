from math import lcm
cases=int(input())

for i in range(cases):
    a,b=map(int,input().split())
    print(lcm(a,b))