#1676 팩토리얼 0의 개수

def cal(n):
    cnt = [0,0]
    while 1:
        if n%2 == 0:
            n = n//2
            cnt[0] += 1
        elif n%5 ==0:
            n=n//5
            cnt[1] += 1
        else:
            return cnt

n = int(input())
cnt_tf = [0,0]
for i in range(1,n+1):
    tmp = cal(i)
    cnt_tf[0] += tmp[0]
    cnt_tf[1] += tmp[1]
answer = min(cnt_tf[0],cnt_tf[1])
print(answer)