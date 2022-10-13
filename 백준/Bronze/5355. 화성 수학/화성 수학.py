cnt=int(input())
eq=['@','#','%']
for i in range(cnt):
    num=input().split()
    result=0
    for j in num:
        if j in eq:
            if j=="@":
                result=result*3
            if j=="%":
                result+=5
            if j=="#":
                result-=7
        else:
            result+=float(j)
    print(format(result, ".2f"))