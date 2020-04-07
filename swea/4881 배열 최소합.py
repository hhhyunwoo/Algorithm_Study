#4881 배열 최소합
#list 값을 바로 변경할 수 없다?
#visited[k][1] = 1 이렇게 직접 변경이 불가능하다.
#map_list = [list(map(int, input().split())) for _ in range(N)]
# use_check = [True for _ in range(N)]
#이문장 어떻게 해석?

def count(idx, visited, SUM):
    global MIN
    if idx >= N:
        if SUM < MIN:
            MIN = SUM
        return
    ###############################
    #가지치기 하는 것 매우중요!!
    #가지치기 안하고 완전탐색했는데 시간초과떴다. 
    #가지치기를 하니깐 바로  PASS,,,
    if SUM > MIN:
        return
    ##############################
    for k in range(0,N):
        if visited[k] == 0: #k번째 값에 접근한적이 없다면
            SUM += maze[idx][k]
            
            visited[k] = 1

            count(idx+1, visited, SUM)
            
            visited[k] = 0 #원상복구
            SUM -= maze[idx][k]


T = int(input())
for TC in range(1,T+1):
    N = int(input())
    maze = list()
    for i in range(N):
        arr = list(map(int,input().split()))
        maze.append(arr)
    

    visited = {}
    for i in range(0,N):
        visited[i] = 0
    SUM = 0
    MIN = 99999

    count(0, visited, SUM)

    print("#%d %d" %(TC, MIN))