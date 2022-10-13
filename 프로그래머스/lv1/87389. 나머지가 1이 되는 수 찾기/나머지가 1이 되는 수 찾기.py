def solution(n):
    answer = 0
    while True:
        answer+=1
        lo= n % answer
        if lo==1:
            return answer