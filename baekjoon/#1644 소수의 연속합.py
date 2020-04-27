#1644 소수의 연속합

def era_prime(N):
    prime = list()
    visited = [0,0] + [1]*(N-1)
    for i in range(2,N+1):
        if visited[i]:
            prime.append(i)
            for j in range(2*i,n+1,i):
                visited[j] = 0
    return prime

if __name__ == "__main__":
    N = int(input())
    arr = era_prime(N)

    s,e = 0,0
    sum = 0
    answer = 0
    while 1:
        if sum >= N:
            sum -= arr[s]
            s += 1
        elif e == len(arr): break
        else:
            sum += arr[e]
            e += 1
        if sum == N:
            answer += 1
    print(answer)