#1759 백준 암호만들기
#문자열에서는 find, 리스트에서는 index를 사용하면 특정 문자 인덱스 반환 가능

def dfs(count,visited, ans):
    if count >= L:
        con1 =0
        con2 = False

        for k in range(0,len(ans)):
            if 'a' == ans[k] or 'e' == ans[k] or 'i' == ans[k] or 'o' == ans[k] or 'u' == ans[k]:
                con2 = True #모음 1개 이상
            else:
                con1 +=1
        
        if con1>=2 and con2 ==True:
            print(ans)
        return
    
    for i in range(0,C):
        P = 0
        if len(ans) > 0:
            P = arr.index(ans[len(ans)-1])
        if visited[i] == 0 and i >= P: #방문안했어야 하고, 바로 앞 문자보다 더 큰 문자여야함.
            visited[i] = 1
            ans += arr[i]
            dfs(count+1, visited, ans)
            visited[i] = 0
            ans = ans[:len(ans)-1] #더했던 값 제거


L, C = map(int,input().split())

arr = list(map(str,input().split()))
arr.sort()

visited = [False for _ in range(C)]
ans = ""

dfs(0,visited, ans)