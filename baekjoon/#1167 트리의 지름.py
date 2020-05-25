#1167 트리의 지름

'''
dfs와 bfs로는 못푸는 문제...?

와씨..... 드릅게 어렵네

문제접근 방식은 
https://blog.myungwoo.kr/112
요기를 참고하시지요...

그리고 입력값에서 from vertex가 순서대로 주어진다는 말이 없다는거,,,,,
ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
시간 엄청 걸렸다.. ㅠㅠ
'''

import sys
from collections import deque

sys.setrecursionlimit(10**9)

MAX = -999999999
MAX_idx = 1

def bfs(arr,val,n):
    global MAX
    global MAX_idx
    queue = deque()
    queue.append(val)
    SUM = [0]*(n+1)
    visited = [0] * (n+1)

    while queue:
        val = queue.popleft()
        visited[val] = 1
        for v in arr[val]:
            if visited[v[0]]==0:
                queue.append(v[0])
                SUM[v[0]] = SUM[val] + v[1]
                if SUM[v[0]] > MAX:
                    MAX = SUM[v[0]]
                    MAX_idx = v[0]

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    answer = 0
    arr = {i:[] for i in range(1,n+1)}
    for i in range(1,n+1):
        val = list(map(int,sys.stdin.readline().split()))
        j = 1
        while 1:
            if val[j] == -1:break
            arr[val[0]].append([val[j],val[j+1]])
            j += 2

    bfs(arr,1,n)
    MAX=0
    bfs(arr,MAX_idx,n)
    print(MAX)