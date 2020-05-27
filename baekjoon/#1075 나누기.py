#1075 나누기

n = input()
f = int(input())

for i in range(0,99):
    if i<=9:
        val = '0'+str(i)
    else: val = str(i)
    tmp = n[:len(n)-2] + val
    if int(tmp)%f == 0:
        print(val)
        break