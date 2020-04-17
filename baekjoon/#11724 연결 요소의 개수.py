#11727 연결 요소의 개수

#시간초과

#시간초과 문제는 dfs를 bfs로 , 간선을 두배로 곱해주고 계산하는 방법을 바꾸면서 해결
'''
즉, 1 2 , 2 1 이런식으로 둘 다 확인하려고 간선을 두배로 더해줬다. 이 부분을 bfs에서 if else 두가지로 나누어서 해결함

근데 계속 50%에서 틀렸다고 나왔다.

반례를 찾아보니

6 2
3 4
4 2
같은 경우 간선이 없는 정점 또한 연결요소로 보고 세어준다는 것이다.

문제 해석에 대한 미숙이 문제였다.

그래서 시작점을 1부터 끝까지 돌려버리는 것이 아니라, 간선을 확인하고 간선의 시작점을 시작점으로 잡고 bfs를 간선의 개수만큼 돌렸다.
그랬더니 완성!
'''


import sys

def bfs(start,visited,flag):
    queue = list()
    queue.append(start)

    while queue:
        start = queue.pop(0)
        for i in range(len(arr)):
            if start in arr[i]:
                if arr[i][0] == start and visited[arr[i][1]] == 0:
                    flag = 1
                    visited[arr[i][1]] = 1
                    queue.append(arr[i][1])

                elif arr[i][1] == start and visited[arr[i][0]] == 0:
                    flag = 1
                    visited[arr[i][0]] = 1
                    queue.append(arr[i][0])

            '''if arr[i][0] == start and visited[arr[i][1]] == 0:
                flag = 1
                visited[arr[i][1]] = 1
                queue.append(arr[i][1])'''
    return flag

if __name__ =="__main__":
    N, M = map(int,sys.stdin.readline().split())
    arr = list()
    for i in range(0,M):
        u, v = map(int,sys.stdin.readline().split())
        arr.append((u,v))
        #arr.append((v,u))
    arr = sorted(arr)

    cnt = 0
    visited = [0 for _ in range(N+1)]
    for j in range(len(arr)):
        start = arr[j][0]
        if visited[start] == 0:
            visited[start] = 1
            flag = bfs(start, visited,0)
            if flag == 1:
                cnt +=1
    for i in range(1,N+1):
        if visited[i] == 0:
            cnt+=1
    print(cnt)

