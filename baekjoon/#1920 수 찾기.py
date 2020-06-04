#1920 수 찾기

'''
당연히 브루트포스로 풀면 안되니깐 정답률이 28프로겠지??

이분탐색느낌..

솔직히 이분탐색이라는 힌트만 얻으면 쉽게 풀수 있는 문제이다.

입력받는 arr값을 정렬해준 다음 이분탐색으로 log(n)의 시간복잡도로 n개를 풀면 nlog(n)이니깐 충분히 가능!
'''

import sys
import operator
input=sys.stdin.readline

def find(target,arr):
   front,rear=0,len(arr)-1
   flag=0
   while rear>=front:
      mid=(front+rear)//2
      if arr[mid] >= target:
         if arr[mid]==target:
            flag=1
            break
         rear=mid-1
      else:
         front=mid+1
   return flag

if __name__ == "__main__":
   n=int(input())
   arr1=list(map(int,input().split()))
   m=int(input())
   arr2=list(map(int,input().split()))

   arr1=sorted(arr1)
   for a in arr2:
      print(find(a,arr1))
