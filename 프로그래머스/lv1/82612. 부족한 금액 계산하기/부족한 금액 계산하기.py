def solution(price, money, count):
    tmp=0
    for i in range(count):
    
        tmp+=(i+1)*price
        
    if money - tmp <0:
        return(tmp-money)
    else:
        return 0
