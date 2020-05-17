#1712 손익분기점
#아주 간단한 수학문제이다. 살짝 너무 코딩스러운 마인드를 가지고 있었다.
# 수학적 부등식으로 접근하면 간단한 문제!

a,b,c = map(int,input().split())

cost = a
n = 0
if c<=b:
    n = -1
else:
    n = a//(c-b) + 1
print(n)