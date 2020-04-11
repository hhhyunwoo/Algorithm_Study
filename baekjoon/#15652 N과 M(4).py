#15652 N과 M(4)

def dfs(cnt,ans):
    if cnt == M:
        print(' '.join(map(str,ans)))
        return
        
    for i in range(1,N+1):
        if not ans:
            ans.append(i)
            dfs(cnt+1, ans)
            ans.pop()
        elif ans and ans[len(ans)-1] <= i:
            ans.append(i)
            dfs(cnt+1, ans)
            ans.pop()

if __name__ == "__main__":
    N, M = map(int,input().split())
    ans = list()
    dfs(0,ans)