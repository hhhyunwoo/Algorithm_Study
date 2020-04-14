#9613 GCD 합
def gcd(a,b):
    while b:
        tmp = a%b
        a = b
        b = tmp
    return a

def lcm(a,b):
    c = gcd(a,b)
    return (a*b)//c

N = int(input())
for _ in range(N):
    arr = list(map(int,input().split()))
    num = arr[0]
    for T in range(num):
        ans = 0
        for j in range(1,len(arr)):
            for k in range(j+1,len(arr)):
                ans += gcd(arr[j], arr[k])
    print(ans)
