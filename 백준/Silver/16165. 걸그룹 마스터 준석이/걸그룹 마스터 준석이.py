grp_num,q_num = map(int,input().split())
grp_name = []
member_name =[]
for i in range(grp_num):
    grp_name.append(input())
    member_num = int(input())
    a=[]
    for j in range(member_num):
        a.append(input())
    member_name.append(a)

dict1 = {grp_name[i]:member_name[i] for i in range(len(grp_name))}
#문제
for k in range(q_num):
    q = input()
    qt = int(input())
    if qt ==1:
        for key,value in dict1.items():
            if q in value:
                print(key)
    if qt ==0:
        for h in sorted(dict1.get(q)):
            print(h)