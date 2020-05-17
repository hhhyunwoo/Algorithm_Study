#1193 분수찾기

a = int(input())
b = 1
i = 1
while 1:
    b +=i
    if b>a:
        b -=i
        break
    i+=1
if i%2 == 0:#짝수
    print(str(1+a-b)+'/'+str(i-a+b))
else:
    print(str(i-a+b)+'/'+str(1+a-b))


