def solution(N, stages):
    res=[]
    for stage in range(1,N+1):
        reached=0
        complete=0
        for j in stages:
            if j>=stage:
                reached+=1
                if j>stage:
                    complete+=1
        if reached ==0:
            fail=1
        else:
            fail=complete/reached
        res.append([fail,stage])
    res.sort()
    print(res)
    return [res[i][1]for i in range(len(res))]
                    
    
