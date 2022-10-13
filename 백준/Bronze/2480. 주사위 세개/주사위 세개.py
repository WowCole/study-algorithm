scores = list(map(int,input().split()))
num=[scores.count(i)for i in scores]

if 3 in num:
    print(10000+(scores[num.index(3)]*1000))
elif 2 in num:
    print(1000+(scores[num.index(2)]*100))
else:
    print(max(scores)*100)