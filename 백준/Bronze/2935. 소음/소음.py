num=[]

for i in range(3):
    num.append(input())

if "*" in num:
    print(int(num[0])*int(num[2]))

if "+" in num:
    print(int(num[0])+int(num[2]))