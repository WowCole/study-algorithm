def solution(numbers):
    answer = []
    i=0
    j=i+1
    while i<len(numbers)-1:
        answer.append(numbers[i]+numbers[j])
        j+=1
        if j==len(numbers):
            i+=1
            j=i+1
    
    return sorted(list(set(answer)))