def solution(left, right):
    answer=0
    while True:
        if left>right:
            return answer
        else:
            tmp=0
            for i in range(left):
                if left%(i+1)==0:
                    tmp+=1
            if tmp%2==0:
                answer+=left
                left+=1
            else:
                answer-=left
                left+=1
                    
                