#15657 N과 M(8)

def dfs(cnt,ans,visited):
    if cnt == M:
        print(' '.join(map(str,ans)))
        return
        
    for i in range(0,len(arr)):
        
        if not ans:
            ans.append(arr[i])
            visited[arr[i]] = 1
            dfs(cnt+1, ans,visited)
            ans.pop()
            visited[arr[i]] = 0
        elif ans and ans[len(ans)-1] <= arr[i]:
            ans.append(arr[i])
            visited[arr[i]] = 1
            dfs(cnt+1, ans,visited)
            ans.pop()
            visited[arr[i]] = 0

if __name__ == "__main__":
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))
    arr = sorted(arr)   
    ans = list()
    visited = [0 for _ in range(10001)]
    dfs(0,ans,visited)