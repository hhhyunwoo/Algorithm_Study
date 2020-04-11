#15651 N과 M(3)

def dfs(cnt, visited,ans):
    if cnt == M:
        print(' '.join(map(str,ans)))
        return
    for i in range(1,N+1):
        ans.append(i)
        dfs(cnt+1, visited, ans)
        ans.pop()
        visited[i] = 0

if __name__ == "__main__":
    N, M = map(int,input().split())
    visited = [0 for _ in range(N+1)]
    ans = list()
    dfs(0,visited,ans)