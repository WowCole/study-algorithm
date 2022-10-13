t=str(input())
cmpr=["c=","c-", "dz=" ,"d-", "lj", "nj", "s=", "z="]
count=0
for i in cmpr:
    count+=t.count(i)
print(len(t)-count)