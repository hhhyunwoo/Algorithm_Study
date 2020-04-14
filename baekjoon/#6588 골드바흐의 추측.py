#6588 골드바흐의 추측
'''
맨첨에는 에라토스테네스의 체를 새로운 list에 append했는데 여기서 시간을 많이 잡아먹은 듯하다.
그냥 arr를 가지고 True로 잘라내면서 남은 False값을 소수로 지정하였다.

2~MAX까지 돌면서 i가 소수이고, N - i 가 소수이면 바로 출력해버리면 끝이다.
생각보다 시간을 많이 잡아먹었다.
'''
import sys

input = sys.stdin.readline

prime = [False] *(1000001)

#####################
# ##에라토스테네스의 체
for i in range(2,1000001):
    if i*i > 1000000: break
    if prime[i] is False:
        for j in range(i*i,1000001, i):
            prime[j] = True
        

while True:
    N = int(input())
    if N == 0: break
    A,B = 0,0
    i = 2
    while True:
        if prime[i] is False:
            j = N-i
            if prime[j] is False:
                A = i
                B = j
                break
        
        i += 1
        '''for j in range(i+1, len(prime)):
            if prime[i] + prime[j] == N:
                A = prime[i]
                B = prime[j]
                break
                if (prime[j] - prime[i])>(B-A):
                    A = prime[i]
                    B = prime[j]
                    continue
            if prime[i] + prime[j] > N:
                break'''
    
    print("%d = %d + %d" %(N,A,B))


