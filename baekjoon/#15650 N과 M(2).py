#15650 N과 M(2)


def dfs(cnt, visited,ans):
    if cnt == M:
        print(' '.join(map(str,ans)))
        #print(*ans)
        return
 
    for i in range(1,N+1):
        if visited[i] == 0:
            if ans and ans[len(ans)-1] < i:
                visited[i] = 1
                ans.append(i)
                dfs(cnt+1, visited, ans)
                ans.pop()
                visited[i] = 0
            elif not ans: #ans에 아무것도 없으면
                visited[i] = 1
                ans.append(i)
                dfs(cnt+1, visited, ans)
                ans.pop()
                visited[i] = 0

if __name__ == "__main__":
    N, M = map(int,input().split())
    visited = [0 for _ in range(N+1)]
    ans = list()
    dfs(0,visited,ans)