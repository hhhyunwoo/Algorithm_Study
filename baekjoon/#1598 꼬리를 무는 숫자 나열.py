#1598 꼬리를 무는 숫자 나열

a,b = map(int,input().split())

arr = [[(a-1)%4,(a-1)//4],[(b-1)%4,(b-1)//4]]
print(abs(arr[0][0]-arr[1][0]) + abs(arr[0][1]-arr[1][1]))