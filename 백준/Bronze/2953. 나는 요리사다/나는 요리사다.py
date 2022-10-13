fin=[]
for i in range(5):
    fin.append(sum([int(i) for i in (input().split())]))

print(fin.index(max(fin))+1,max(fin))