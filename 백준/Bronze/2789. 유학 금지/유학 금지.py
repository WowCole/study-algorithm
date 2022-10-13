comp="CAMBRIDGE"
a=str(input())
b=str()
for i in a:
    if not i in comp:
        b+=i
print(b)