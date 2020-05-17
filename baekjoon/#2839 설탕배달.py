#2839 설탕배달

a = int(input())
flag = 0
for i in range(0,1668):
    for j in range(0,1001):
        if i*3 + j*5 == a:
            flag = 1
            answer = i+j
            break
    if flag == 1:
        print(answer)
        break
if flag == 0:
    print(-1)
