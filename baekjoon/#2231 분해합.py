#2231 분해합

def check(a):
    tmp = 0
    while a>0:
        tmp += a%10
        a //= 10
    return tmp

n = int(input())

idx = 1
flag = 0
while idx <= 1000000:
    tmp = idx + check(idx)
    if tmp == n:
        print(idx)
        flag = 1
        break
    idx += 1
if flag == 0:
    print(0)