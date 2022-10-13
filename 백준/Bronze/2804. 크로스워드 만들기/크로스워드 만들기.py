a,b=map(str,input().split())
for i in range(len(a)):
    if a[i] in b:
        break
wn = b.find(a[i])

for j in range(len(b)):
    if j == wn:
        print(a)
    else:
        print("."*i+b[j]+"."*(len(a)-i-1))