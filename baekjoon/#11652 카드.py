#11652 카드
from collections import Counter
N = int(input())
arr = [int(input()) for _ in range(N)]

oft = Counter(arr).most_common()


same = list()
same.append(oft[0][0])
if len(oft)>1 and oft[0][1] == oft[1][1]:
    i = 1
    while 1:
        same.append(oft[i][0])

        if i>=len(oft)-1:break
        if oft[i][1] != oft[i+1][1]:
            break
        
        i += 1

same = sorted(same,key=lambda k:k)
oft_ans = same[0]

print(oft_ans)