#16948 데스 나이트

dy = [-2,-2,0,0,2,2]
dx = [-1,1,-2,2,-1,1]

def bfs(r1,c1,r2,c2):
    queue = list()
    queue.append((r1,c1))
    visited = [[0 for _ in range(N)]for _ in range(N)]
    visited[r1][c1] = 1
    
    while queue:
        pos = queue.pop(0)
        y = pos[0]
        x = pos[1]
        if y==r2 and x==c2:
            break
        for dir in range(0,6):
            ny = y+dy[dir]
            nx = x+dx[dir]
            if 0<=ny<N and 0<=nx<N and visited[ny][nx] ==0:
                queue.append((ny,nx))
                visited[ny][nx] = visited[y][x] + 1
    return visited[r2][c2]

if __name__ == "__main__":
    N = int(input())
    r1,c1,r2,c2 = map(int,input().split())

    answer = bfs(r1,c1,r2,c2)
    print(answer-1)