#10872 팩토리얼
#0!이 1이라니....
answer = 1
def fac(N):
    global answer
    if N <= 0:
        print(answer)
        return 
    answer *= N
    fac(N-1)

N = int(input())

fac(N)