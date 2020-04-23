#10845 큐

from collections import deque
import sys

N = int(input())
queue = deque()
for i in range(N):
    comm = sys.stdin.readline().split()

    if comm[0] == "push":
        queue.append(comm[1])
    elif comm[0] == "pop":
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif comm[0] == "size":
        print(len(queue))
    elif comm[0] == "empty":
        if not queue:
            print(1)
        else:
            print(0)
    elif comm[0] == "back":
        if not queue:
            print(-1)
        else:
            print(queue[-1])
    elif comm[0] == "front":
        if not queue:
            print(-1)
        else:
            print(queue[0])
