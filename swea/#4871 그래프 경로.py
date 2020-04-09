#4871 그래프 경로
def dfs(graph, start, end):
    visited = list()
    stk = list()
    stk.append(start)
    while stk:
        node = stk.pop()
        if node not in visited:
            visited.append(node)
            stk += graph[node] - set(visited)
    #print(visited)
    if end in visited:
        return 1
    else :
        return 0

T = int(input())

for TC in range(1, T + 1):
    V, E = map(int, input().split())
    adj = {1:set([])}
    for j in range(2,V+1):  #vertex 개수만큼 딕셔너리 추가
        adj[j] = set([])
#    undirected graph
#    graph = {'A': set(['B', 'C']),
#       'B': set(['A', 'D', 'E']),
#       'C': set(['A', 'F']),
#       'D': set(['B']),
#       'E': set(['B', 'F']),
#       'F': set(['C', 'E'])}
    
    for i in range(E): 
        start, end = map(int,input().split())
        adj[start].add(end)

    A,B = map(int, input().split())
    print("#%d %d" %(TC, dfs(adj, A, B)))