#1550 16진수

arr = input()
res,idx= 0,0
for a in arr[::-1]:
    if a.isdigit():
        res += int(a)*16**idx
    else:
        res+=(10+ord(a)-ord('A'))*16**idx
    idx+=1
print(res)

#print(int(input(),16))