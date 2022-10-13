
num=int(input())
def slc(num):
    tmp=2
    while 2 <= num:
        if num%tmp==0:
            print(tmp)
            num=num/tmp
        else:
            tmp+=1
slc(num)