#1297 tv 크기
import math
arr = list(map(int,input().split()))
c = math.sqrt(arr[1]**2+arr[2]**2)
c = arr[0]/c
print(math.floor(arr[1]*c), math.floor(arr[2]*c)) 