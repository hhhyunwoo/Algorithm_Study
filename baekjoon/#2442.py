#2442

N = int(input())
ans=""
for i in range(0,N):
    for j in range(0,N-i-1): ans += " "
    for j in range(0,2*i+1): ans += "*"
    print(ans)
    ans = ""
        