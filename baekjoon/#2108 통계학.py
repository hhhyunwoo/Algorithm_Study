#2108 통계학
import math
import sys
from collections import Counter

N = int(sys.stdin.readline())
arr=[int(input()) for _ in range(N)]
arr = sorted(arr,key=lambda k: k)
oft = Counter(arr).most_common()

oft_ans = oft[0][0]
if len(oft) >1 and oft[0][1] == oft[1][1]:
    oft_ans = oft[1][0]


SUM = sum(arr)
AVG = round(SUM/N)
MIN = min(arr)
MAX = max(arr)

print(AVG) #평균 소수점 이하 첫째자리에서 반올림하기
print(arr[N//2])
print(oft_ans)
print(MAX - MIN) #범위
