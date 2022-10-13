N = int(input())
files = [input() for i in range(N)]
answer = '' # answer를 비어있는 문자열로 초기화 합니다.
for idx in range(len(files[0])): # 0번째 글자 ~ i번째 글자 판단
    allsame = True
    for kth in range(N):
        if files[kth][idx] != files[0][idx]:
            allsame = False
    if allsame == True: # idx 번째 글자가 모두 같으면
        answer += files[0][idx]
    else: # 다른게 하나라도 있다면
        answer += '?'
print(answer)