#2178 미로 탐색


'''
맨 처음에는 시작점에서 끝점으로 가는 것이기 때문에 당연히 DFS로 쭉 파고드는 것이라 생각했다.
그런데 1프로에서 안가다가 계속 시간초과로 터졌다.

조금 찾아보니 최단 거리는 무조건 BFS라고 한다!
DFS같은 경우는 최단 거리로 엄청나게 많은 경우의 수가 나오기 때문에 시간복잡도가 지수가 나온다.

그래서 BFS로 구현을 하는데 아무리 생각해도 접근법이 이해가 안되었다. 

COUNT를 어떤식으로 해야하지?
큐에 append할때 count를 해버리니 모든 갈 수있는 경우에 다 count를 해버렸다.

그래서 visited를 이용하는 것이다!
visited가 단순히 방문했다는 것을 의미하는 것이 아니라, 이전의 길에서 현재의 길까지 오는  길이를 체크하는 것이다.

조금 다른 접근법이었다.

원래 미로 찾기에서 BFS를 사용할 때 visited를 안쓰고 MAP의 값을 0으로 주어서 못가게 만들었었는데 이번 문제는 거리를 측정하는 것이기 때문에 조금 다른 방법을 적용해야 했던 것 같다.

쉬운문제인 줄 알았는데 조금 어색해서 힘들었다.

미로 최단 거리 문제 중 아주 전형적인 문제이다. 
나중에 몇 번 더 풀어봐야겠다!
'''
import sys
dy = [-1,1,0,0]
dx = [0,0,-1,1]
answer = 99999999

def bfs(y,x,visited):
    queue = list()
    queue.append((y,x))
    cnt = 0
    newy,newx = 0,0

    while queue:
        pos = queue.pop(0)
        cnt += 1
        y = pos[0]
        x = pos[1]
        if y == N-1 and x == M-1:
            return visited[y][x]

        for dir in range(0,4):
            newy = y+dy[dir]
            newx = x+dx[dir]
            if 0<=newy<N and 0<=newx<M and visited[newy][newx] == 0 and MAP[newy][newx] == 1:
                queue.append((newy,newx))
                visited[newy][newx] = visited[y][x] + 1


def dfs(y,x,visited,cnt):
    global answer
    if y == (N-1) and x == (M-1):
        answer = min(answer,cnt)
        return
    if cnt >= answer:
        return

    for dir in range(0,4):
        newy = y+dy[dir]
        newx = x+dx[dir]
        if 0<=newy<N and 0<=newx<M and visited[newy][newx] == 0 and MAP[newy][newx] == 1:
            visited[newy][newx] = 1
            dfs(newy,newx,visited,cnt+1)
            visited[newy][newx] = 0

if __name__ == "__main__":
    N,M = map(int,sys.stdin.readline().split())
    MAP = [[0 for _ in range(M)] for _ in range(N)]
    arr = [str(sys.stdin.readline()) for _ in range(N)]
    for i in range(0,N):
        for j in range(0,M):
            MAP[i][j] = int(arr[i][j])
    
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[0][0] = 1
    #dfs(0,0,visited,1)
    answer = bfs(0,0,visited)
    print(answer)
    