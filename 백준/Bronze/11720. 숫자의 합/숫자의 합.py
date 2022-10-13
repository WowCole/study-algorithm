t=int(input())
b=int(input())
num="1"
a=0
for i in range(t):
    a+= b//int(num+"0"*(t-i-1))
    b= b%int(num+"0"*(t-i-1))

print(a)
    