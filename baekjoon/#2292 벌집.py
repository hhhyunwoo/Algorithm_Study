#2292 벌집

a = int(input())
dp = [0,1]
i=2
while 1:
    dp.append(dp[i-1] + i)
    if dp[i]>a:
        break
    i+=1
    

if a ==1:
    print(1)
else:
    for i in range(0,len(dp)):
        if dp[i] > ((a-2)//6):
            print(i+1)
            break
        elif dp[i] == ((a-2)//6):
            print(i+2)
            break