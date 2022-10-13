cost,cnt,money = map(int,input().split())

pm = cost*cnt -money

if pm <= 0:
    pm = 0

print(pm)