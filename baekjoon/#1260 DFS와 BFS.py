#1260 DFS와 BFS

def dfs(start,visited,path):
    path.append(start)
    for i in range(len(arr)):
        if arr[i][0] == start:
            if visited[arr[i][1]] == 0:
                 visited[arr[i][1]] = 1
                 dfs(arr[i][1], visited, path)
    return path

def bfs(start,path):
    queue = list()
    queue.append(start)
    path.append(start)

    while queue:
        start = queue.pop(0)
        for i in range(len(arr)):
            if arr[i][0] == start and visited[arr[i][1]] == 0: 
                path.append(arr[i][1])
                queue.append(arr[i][1])
                visited[arr[i][1]] = 1
    return path

if __name__ == "__main__":
    N, M, V = map(int,input().split())
    
    arr = list()
    for i in range(0,M):
        S, E = map(int,input().split())
        arr.append((S,E))
        arr.append((E,S))
    
    arr = sorted(arr)

    visited = [0 for _ in range(N+1)]
    visited[V] = 1
    path = list()
    path = dfs(V, visited,path)
    print(*path)

    visited = [0 for _ in range(N+1)]
    visited[V] = 1
    path = list()
    path = bfs(V,path)
    print(*path)