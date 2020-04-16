#4963 섬의 개수

dy = [-1,1,0,0,-1,-1,1,1]#상하좌우 좌상, 우상, 좌하, 우하
dx = [0,0,-1,1,-1,1,-1,1]#상하좌우 좌상, 우상, 좌하, 우하

def bfs(y,x):
    queue = list()
    cnt = 0

    for row in range(0,M):
        for col in range(0,N):
            if MAP[row][col] == 1:
                y = row
                x = col
                queue.append((y,x))
                cnt += 1
                while queue:
                    pos = queue.pop(0)
                    y = pos[0]
                    x = pos[1]
                    for dir in range(8):
                        newy = y + dy[dir]
                        newx = x + dx[dir]
                        if 0<=newy<M and 0<=newx<N and MAP[newy][newx] == 1:
                            queue.append((newy,newx))
                            MAP[newy][newx] = 2
    return cnt


if __name__ == "__main__":
    while 1:
        N, M = map(int,input().split())
        if N==0 and M == 0:
            break

        MAP = [list(map(int,input().split())) for _ in range(M)]
        cnt = bfs(0,0)
        print(cnt)
