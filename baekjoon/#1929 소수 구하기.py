#1929 소수 구하기
#1000000
def make_prime(N,M):
    prime = []
    arr = [False, False] + [True]*(M-1)
    for i in range(2,M+1):
        if arr[i]:
            prime.append(i)
            for j in range(2*i,M+1,i):
                arr[j] = False
    return prime

if __name__ == "__main__":
    a,b = map(int,input().split())
    res = make_prime(a,b)
    for i in range(0,len(res)):
        if a <= res[i] <=b:
            print(res[i])