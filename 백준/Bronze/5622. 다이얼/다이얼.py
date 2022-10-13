line = str(input())
alph = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
num = [3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10]
dial = {alph[i]: num[i] for i in range(len(alph))}
count=0
for i in line:
    count+=dial.get(i)
print(count)
