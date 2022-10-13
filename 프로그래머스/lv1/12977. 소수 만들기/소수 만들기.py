def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

def solution(nums):
    arr1=[]
    res=[]
    answer=0
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                arr1.append([nums[i],nums[j],nums[k]])
                
    for i in arr1:
        res.append(sum(i))
    
    for i in res:
        if is_prime_number(i) == True:
            answer+=1
    return answer