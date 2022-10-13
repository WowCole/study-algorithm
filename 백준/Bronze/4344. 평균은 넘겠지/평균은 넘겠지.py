t = int(input())
for i in range(t):
    total=[int(i) for i in (input().split())]
    st_num=total[0]
    score=total[1:]
    avg=sum(score)/st_num
    count=0
    for i in score:
        if i > avg:
            count+=1
        res = count/st_num*100
    print("%0.3f%%" % res)