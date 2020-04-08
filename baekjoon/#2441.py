#2441

N = int(input())
ans = list()
for i in range(N):
    ans.append("*")
for i in range(0,N):
    print(''.join(ans))
    ans[i] = " "