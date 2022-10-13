def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        num1=format(arr1[i],'b')
        num2=format(arr2[i],'b')
        while len(num1)<n or len(num2)<n:
            if len(num1)<n:
                num1="0"+num1
            if len(num2)<n:
                num2="0"+num2
        result=""
        for j in range(n):
            if int(num1[j])+int(num2[j])>0:
                result+="#"
            else:
                result+=" "
        answer.append(result)
    return answer