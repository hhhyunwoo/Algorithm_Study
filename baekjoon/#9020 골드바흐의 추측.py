#9020 골드바흐의 추측

import sys

input = sys.stdin.readline

prime = [False] *(10001)

#####################
# ##에라토스테네스의 체
for i in range(2,10001):
    if i*i > 10000: break
    if prime[i] is False:
        for j in range(i*i,10001, i):
            prime[j] = True
        

T = int(input())
for _ in range(T):
    N = int(input())
    i = N//2

    while True:
        if prime[i] is False:
            j = N-i
            if prime[j] is False:
                A = i
                B = j
                break
        
        i -= 1
    print("%d %d" %(A,B))


