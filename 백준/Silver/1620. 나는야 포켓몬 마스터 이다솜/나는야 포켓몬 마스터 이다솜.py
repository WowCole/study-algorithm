mons_cnt,q_cnt= map(int,input().split())
mons_nm=[input() for i in range(mons_cnt)]
mon_dict={mons_nm[i]: i+1 for i in range(mons_cnt)}
mon_no={i+1 : mons_nm[i] for i in range(mons_cnt)}
for i in range(q_cnt):
    ans = input()
    if ans.isdigit():
        print(mon_no.get(int(ans)))
    else:
        print(mon_dict.get(ans))