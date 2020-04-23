#10808 알파벳 개수

#딕셔너리 출력하는 방법 알아놓기!

arr = str(input())
alp = {'a':0}
val = 'a'
for i in range(0,25):
    val = chr(ord(val)+1)
    alp[val] = 0

for i in range(0,len(arr)):
    alp[arr[i]] += 1

for value in alp.values():
    print(value, end=' ')