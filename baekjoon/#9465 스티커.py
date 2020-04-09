#9465 스티커
#완전탐색 가능? 0<=N <= 100,000
#ㄴㄴ 불가능
#점화식 세우기 어려운데??
#하나의 점으로 올 수 있는 루트가 대각선과 두선 대각선 밖에없다. 모두의 경우의 수를 DP로 구하면 되는데,, ,점화식 세우기 생각보다 까다로움,,,

if __name__ == "__main__":
    T = int(input())
    for TC in range(T):
        N = int(input())
        maze = [[0 for _ in range(N+1)] for _ in range(2)]
        for i in range(0,2):
            arr = list(map(int,input().split()))
            for j in range(1,N+1):
                maze[i][j] = arr[j-1]
        
        for k in range(2,N+1):
            maze[0][k] += max(maze[1][k-2], maze[1][k-1])
            maze[1][k] += max(maze[0][k-2], maze[0][k-1])
        ans = max(maze[0][N], maze[1][N])
        print(ans)
    