
a=int(input())
b=str(input())
for i in range(len(b)):
    print(a*int(b[len(b)-1-i]))
print(a*int(b))