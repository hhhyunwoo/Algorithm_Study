#1316 그룹 단어 체커

n = int(input())
arr = [str(input()) for _ in range(n)]
cnt=0
for val in arr:
    tmp = []
    flag = 0
    for i in range(0,len(val)):
        if val[i] in tmp:
            if val[i-1] != val[i]:
                flag = 1
                break
        tmp.append(val[i])
    if flag == 0:
        cnt+=1
print(cnt)