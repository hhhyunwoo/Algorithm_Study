#4843 특별한 정렬


T = int(input())
for TC in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = list()
    while len(arr) > 0:
        top = max(arr)
        arr.remove(top)
        ans.append(top)

        bot = min(arr)
        arr.remove(bot)
        ans.append(bot)
    result = ' '.join(map(str,ans[0:10]))

    print("#%d" %TC,result)