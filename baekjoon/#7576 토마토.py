#7576 토마토
'''
맨첨에는 단순하게 bfs, dfs안쓰고 main문안에서 while 문안에서 2중포문을 돌렸다. 당연히 시간초과 발생
bfs로 접근하지 못했던 것은 1이 여러개가 있다면 어떻게 병렬적으로 진행할 것인가? 라는 문제때문에 쓰지못했다.

근데 시간초과 나고 보니깐 무조건 bfs사용해야 할 것 같아서 접근을 visited를 사용하여 걸리는 거리를 측정했다.
계속 1씩 증가하면서 MAP에 있는 visited 중에서 가장 큰 값을 가지고 계산했다.

근데도 시간초과 발생.../
어찌합니까,,,

그래서 좀 찾아보니깐 단순 list로 구현한 queue와 collection의 dequeue와 시간 복잡도 차이가 난다는 것을 알게되었고 , list 대신에 dequeue의 popleft를 사용하니깐 99프로 까지 진행되었다.

*collections.dequeue.popleft() -> O(1)

list.pop(0) -> O(N)


근데 갑자기 99프로에서 런타임이 발생했다.

일단 런타임의 이유는 exit(1) 을 사용해서이다.

flag를 사용해서 해결했는데 100프로에서 틀렸습니다가 발생...

흑흑



77ㅑ

마지막 반례는 바보같이 문제를 잘못 봐서 생긴 일,,,,,

토마토가 다 익어있으면 1이 아니라 0을 출력해야한다. ㅎㅎ

어쨌든 풀이완료!
생각보다 시간이 오래걸렸다 ㅜㅜ

'''
import copy
import sys
import collections

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs():
    queue = collections.deque()
    visited = [[0 for _ in range(M)]for _ in range(N)]
    for i in range(0,N):
        for j in range(0,M):
            if MAP[i][j] == 1:
                queue.append((i,j))
                visited[i][j] = 1
            if MAP[i][j] == -1:
                visited[i][j] = -1
                
    while queue:
        pos = queue.popleft()
        y = pos[0]
        x = pos[1]
        for dir in range(0,4):
            newy = y + dy[dir]
            newx = x + dx[dir]
            if 0<=newy<N and 0<=newx<M and MAP[newy][newx] == 0:
                MAP[newy][newx] = 1
                queue.append((newy,newx))
                visited[newy][newx] = visited[y][x] + 1
    return visited

if __name__ == "__main__":
    M, N = map(int,sys.stdin.readline().split())
    MAP = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

    flag = 1
    for i in range(0,N):
        for j in range(0,M):
            if flag == 0 or MAP[i][j] == 0:
                flag = 0
                break
    
    if flag == 1: #토마토가 다 익어있으면
        print(0)

    elif flag == 0:
        visited = bfs()
        cnt = 0
        for i in range(0,N):
            for j in range(0,M):
                if flag == 1 or visited[i][j] == 0:
                    flag = 1
                    break

        for i in range(0,N):
            if cnt < max(visited[i]):
                cnt = max(visited[i])

        
        if flag == 1:
            print(-1)
        elif cnt == 1:
            print(1)
        else:
            print(cnt-1)



    '''while 1:
        flag = 0
        for j in range(0,N): #다 된지 체크! try except으로 시간줄일 수 있을듯
            for i in range(0,M):
                if MAP[j][i] == 0:
                    flag = 1
                    break
        if flag == 0: 
            print(cnt)
            break

        if cnt > N*M: #안되면
            print(-1)
            break

        for y in range(0,N):
            for x in range(0,M):
                if MAP[y][x] == 1:
                    for dir in range(0,4):
                        newy = y + dy[dir]
                        newx = x + dx[dir]
                        if 0<=newy<N and 0<=newx<M and MAP2[newy][newx] == 0:
                            MAP2[newy][newx] = 1    #MAP2에다가 함. 왜냐면 cnt가 잘 안될 것 같아서.
        MAP = copy.deepcopy(MAP2)
        cnt += 1'''
