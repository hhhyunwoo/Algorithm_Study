#2581 소수


def era(n):
    check = [False, False] + [True]*(n)
    prime = []

    for i in range(0, n+2):
        if check[i]:
            prime.append(i)
            j = i*2
            while j <= n:
                check[j] = False
                j += i
    return prime

if __name__=="__main__":
    m = int(input())
    n = int(input())
    prime = era(n)
    idx_m,idx_n = -1,-1
    for i in range(0, len(prime)):
        if idx_m == -1 and prime[i] >= m:
            idx_m = i
        if idx_n == -1 and prime[i] >= n:
            if prime[i] == n:
                idx_n = i
            else:
                idx_n = i-1
            break

    if idx_m>idx_n:
        print(-1)
    else:
        print(sum(prime[idx_m:idx_n+1]))
        print(min(prime[idx_m:idx_n+1]))
