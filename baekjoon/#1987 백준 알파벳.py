#1987 백준 알파벳
#가지치기
#not in visited 이거도 for 문형식으로 한바퀴 다도는듯. 그래서 시간초과 나온 것 같다.
#alp = chr(ord("A") + i) 
#ord : 아스키코드를 반화나
#chr 숫자에 맞는 아스키 코드를 반환
def game(cnt, x,y):
    global MAX


    for i in range(0,4):
        newx = x + dx[i]
        newy = y + dy[i]

        if 0<=newx<C and 0<=newy<R: #좌표안에있어야함
            value = ord(MAP[newy][newx]) - ord('A')
            if visited[value] == 0: #방문안했다면
                visited[value] = 1
                game(cnt+1, newx, newy)
                visited[value] = 0
    MAX = max(MAX, cnt)

if __name__ == "__main__" :
    R, C = map(int,input().split())
    MAP = list()

    for i in range(0,R):
        arr = str(input())
        MAP.append(arr)

    visited = [0] * 26

    visited[ord(MAP[0][0])-ord('A')] = 1#시작점

    MAX = -9999

    dy = [-1,1,0,0]
    dx = [0,0,-1,1]

    game(1,0,0)

    print(MAX)
