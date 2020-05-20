#1009 분산처리

'''
모든 1의자리 수의 값들의 제곱값은 4자리 안에 반복이 나온다...
'''

def check(n,b):
    if b == 0: b=4
    idx = 1
    tmp = n
    while idx<b:
        tmp = (tmp*n)%10
        idx += 1
    return tmp

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
for a in arr:
    res = check(a[0]%10,a[1]%4)
    if res == 0:
        print(10)
    else:
        print(res)

'''
1111
2486
3971
4646
5555
6666
7931
8426
9191
0000'''