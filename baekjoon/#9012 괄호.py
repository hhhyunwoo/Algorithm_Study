#9012 괄호

#str(input())으로 받으니깐 개행문자 까지 받아버린다.
#그냥 input().split()으로 하자... 리스트로 받아짐

import sys

N = int(input())
for i in range(N):
    flag = 0
    stack = list()
    comm = sys.stdin.readline()

    for j in range(0,len(comm)-1):
        if comm[j] == '(':
            stack.append(comm[j])
        else:
            if not stack:
                flag=1
                break
            stack.pop()
            
    if stack:
        flag = 1

    if flag == 1:
        print("NO")
    else:
        print("YES")