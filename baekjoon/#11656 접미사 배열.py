#11656 접미사 배열

arr = str(input())
answer = list()
for i in range(0,len(arr)):
    answer.append(arr[i:])
answer.sort()
for i in range(0,len(answer)):
    print(answer[i])