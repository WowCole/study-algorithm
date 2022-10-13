t=int(input())
for i in range(t):
    nums=int(input())
    list1=[]
    list2=[]
    for j in range(nums):
        list1.append(str(input()))
    for i in range(len(list1)):
        for j in range(len(list1)):
            if i!=j:
                result = list1[i]+list1[j]
                if result == result[::-1]:
                    list2.append(list1[i]+list1[j])
    if len(list2) == 0:
        print(0)
        list2=[]
    else:
        print(list2[0])