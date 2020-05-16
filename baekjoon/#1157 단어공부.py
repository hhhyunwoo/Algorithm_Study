#1157 단어공부

from collections import Counter

arr = str(input()).upper()


res = Counter(arr).most_common()
MAX = res[0][1]
cnt = 0
flag = 0
for c in res:
    if c[1] == MAX:
        cnt += 1
    if cnt>1:
        flag = 1
        break
if flag == 1:
    print('?')
else:
    print(res[0][0])