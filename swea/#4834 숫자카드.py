#4834 숫자카드

T = int(input())
for TC in range(1, T+1):
    num = int(input())
    N = str(input())
    cnt = []
    for i in range(10):
        cnt.append(0)

    for i in range(num):
        cnt[int(N[i])] += 1

    max = -1
    for i in range(10):
        if cnt[i] >= max:
            ans = i
            max = cnt[i]
    print("#%d %d %d" %(TC, ans, cnt[ans]))
 