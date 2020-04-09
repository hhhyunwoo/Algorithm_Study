#1100 하얀칸

MAP = [[0 for _ in range(8)] for _ in range(8)]

for i in range(0,8):
    if i ==0: flag = 0
    elif flag == 1: flag = 0
    else: flag = 1
    for j in range(0,8):
        if flag == 1: 
            MAP[i][j] = False
            flag = 0
        else: 
            MAP[i][j] = True #흰색
            flag = 1

cnt = 0
for i in range(0,8):
    string = str(input())
    for j in range(0,8):
        if MAP[i][j] == True and string[j] == 'F':
            cnt += 1
print(cnt)