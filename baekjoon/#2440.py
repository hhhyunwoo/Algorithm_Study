#2440
N = int(input())
ans = ""
for i in range(N):
    ans += "*"

for i in range(N,0,-1):
    print(ans)
    ans = ans[:i-1]