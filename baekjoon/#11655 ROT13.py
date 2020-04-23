#11655 ROT13

arr = str(input())
answer = list()

for i in range(0,len(arr)):
    if arr[i].islower():
        val = ord(arr[i]) + 13
        if val > ord('z'):
            answer.append(chr(val-26))
        else:
            answer.append(chr(val))
        #answer.append(chr(ord('a') + ((ord(arr[i]) + 13)%ord('a')) ))
    elif arr[i].isupper():
        val = ord(arr[i]) + 13
        if val > ord('Z'):
            answer.append(chr(val-26))
        else:
            answer.append(chr(val))
    else:
        answer.append(arr[i])

print(''.join(answer))
