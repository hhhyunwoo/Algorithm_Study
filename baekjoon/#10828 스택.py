#10828 스택
import sys

N = int(input())
stack = list()
for i in range(N):
    comm = sys.stdin.readline().split()

    if comm[0] == "push":
        stack.append(comm[1])
    elif comm[0] == "pop":
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif comm[0] == "size":
        print(len(stack))
    elif comm[0] == "empty":
        if not stack:
            print(1)
        else:
            print(0)
    elif comm[0] == "top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])