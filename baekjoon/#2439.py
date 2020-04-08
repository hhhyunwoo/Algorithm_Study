#2439
N = int(input())
ans = list()
for i in range(N):
    ans.append(" ")
for i in range(N,0,-1):
    ans[i-1] = "*"
    print(''.join(ans))