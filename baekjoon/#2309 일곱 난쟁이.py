#2309 일곱 난쟁이

def dfs(visited, SUM, cnt):
    if cnt == 7:
        if  SUM == 100:
            ans = list()
            for j in range(1,10):
                if visited[j] == 1:
                    ans.append(arr[j])
            ans = sorted(ans)
            for k in range(0,7):
                print(ans[k])
            exit()
        return
    

    for i in range(1,10):
        if visited[i] == 0:
            SUM += arr[i]
            visited[i] = 1
            dfs(visited,SUM, cnt + 1)
            SUM -= arr[i]
            visited[i] = 0


visited = [0 for _ in range(10)]

arr = [0 for _ in range(10)]
for i in range(1,10):
    arr[i] = int(input())
dfs(visited, 0, 0)