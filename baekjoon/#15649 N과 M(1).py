#15649 N과 M(1)
#join 쓸때 리스트 값이 int 라면 불가능!
#그래서 map으로 str으로 변환해주고, join해야 string으로 만들 수 있다.

def dfs(cnt, visited,ans):
    if cnt == M:
        print(' '.join(map(str,ans)))
        #print(*ans)
        '''string = ""
        for j in range(0,len(ans)):
            string += str(ans[j])
            string += " "
        print(string)'''
        return
    for i in range(1,N+1):
        if visited[i] == 0:
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