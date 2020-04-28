#4008 swea 숫자 만들기

'''
처음에 바로 순열로 접근했는데 시간초과 계속 뜬다... 백준 문제는 바로 permutation으로 쉽게 풀었는데 ㅜㅜ

아마도 ++ 이렇게 겹치는 문자들이 나오면 순열통해서 나온 것들 중에 중복이 매우 많이 발생해서 그런것 같다. 그래서 permutation 값을 set으로 중복 제거하고 계산했는데도 계속 시간초과가 발생하였다.
permutation 연산자체가 시간이 꽤 걸리는 듯 하다.

그래서 조금 헤매다가 결국 dfs로 풀었다....

나눗셈 같은 경우 헤매다가 조금 찾아봐서 int(a/b) 이렇게 접근하면 파이썬 형식의 나눗셈이 아니라 우리가 일반적으로 아는 나눗셈 연산이 진행된다.

되게 빨리 풀 수 있을 거라 생각했는데 시간이 꽤 걸렸다 ㅜㅜㅜ
'''

from itertools import permutations
MAX = -999999999
MIN = 999999999
def dfs(arr, op_list,op):
    global MAX, MIN
    if sum(op_list) == 0:
        MAX = max(MAX,cal(arr,op))
        MIN = min(MIN,cal(arr,op))
        return
    
    for i in range(0,4):
        if op_list[i] != 0:
            op_list[i] -= 1
            op.append(i)
            dfs(arr,op_list,op)
            op.pop()
            op_list[i] += 1


def cal(arr,val):
    sum = arr[0]
    for i in range(0,len(val)):
        if val[i] == 0:
            sum += arr[i+1]
        elif val[i] == 1:
            sum -= arr[i+1]
        elif val[i] == 2:
            sum *= arr[i+1]
        elif val[i] == 3:
            sum = int(sum/arr[i+1])
            
    return sum

if __name__ == "__main__":
    T = int(input())
    for TC in range(1,T+1):
        MAX = -999999999
        MIN = 999999999
        N = int(input())
        op_list = list(map(int,input().split()))
        arr = list(map(int,input().split()))

        dfs(arr,op_list,[])

        print("#%d %d" %(TC,MAX-MIN))
