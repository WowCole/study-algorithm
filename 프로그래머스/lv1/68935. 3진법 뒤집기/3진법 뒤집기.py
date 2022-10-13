def solution(n):
    num=[]
    answer=0
    while True:
        a=n//3
        b=n%3
        num.append(b)
        if a==0:
            break
        else:
            n=a 
    for i in range(len(num)):
        answer+=num[i]*(3**(len(num)-(i+1)))
    return answer