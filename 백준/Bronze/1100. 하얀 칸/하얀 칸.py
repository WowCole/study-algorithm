chess=[list(input()) for i in range(8)]
count=0
for row in range(8):
    for line in range(8):
        if (row%2==0 and line%2==0) or (row %2 !=0 and line%2!=0):
            if chess[row][line] == "F": 
                count+=1
print(count) 
