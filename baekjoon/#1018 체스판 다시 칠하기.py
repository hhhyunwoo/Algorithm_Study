#1018 체스판 다시 칠하기

n,m = map(int,input().split())
MAP = [str(input()) for _ in range(n)]
answer = 999999999
for y in range(0,n-7):
    for x in range(0,m-7):
        if MAP[y][x] == 'W':
            start = 'W'
            end = 'B'
        else:
            start = 'B'
            end = 'W'

        tmp = start #시작점이 맞다는 기준
        cnt = 0
        for i in range(y,y+8):
            for j in range(x,x+8):
                if MAP[i][j] != tmp:
                    cnt += 1
                if j!=x+7:
                    if tmp == start:
                        tmp = end
                    else:
                        tmp = start
        answer = min(answer,cnt)

        tmp = end#시작점이 틀리다는 기준
        cnt = 0
        for i in range(y,y+8):
            for j in range(x,x+8):
                if MAP[i][j] != tmp:
                    cnt += 1
                if j!=x+7:
                    if tmp == start:
                        tmp = end
                    else:
                        tmp = start
        answer = min(answer,cnt)
        
print(answer)

'''
8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
BWBWBWBW
BWBWBWBW
'''