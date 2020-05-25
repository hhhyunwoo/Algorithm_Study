#11728 배열 합치기
import sys
n,m = map(int,sys.stdin.readline().split())
arr_a = list(map(int,sys.stdin.readline().split()))
arr_b = list(map(int,sys.stdin.readline().split()))

arr_a.extend(arr_b)
arr_a.sort()
print(*arr_a)