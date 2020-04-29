#4012 swea 요리사
from itertools import permutations,combinations
import copy

'''
왜이렇게 잘 안풀리는지 모르겠다.
아주 간단한 문제인데./

맨첨에는 1쌍씩 즉, 2개씩 뽑아서 하는 문제인 줄 알고 계속 헤맸다.
그담에는 알고리즘 기법을 N개로 조합을 만들어서 시간초과 계속 뜨고,,, 조합 함수 문제인줄 알고 dfs로 바꿔서 했는데도 계속 시간초과 뜨고,,, 

흠,, dfs는 왜 시간초과 뜬지 모르겠다. 다시봐야겠다.
조합으로 접근했을때는 계속 이상하게 N개로 접근해서 시간초과 발생했다.

아주 간단한 문제인데 요즘 집중이 잘 안된다 ㅜㅜㅜ
'''


MIN = 99999999999
def check(val1,val2,MAP):
    global MIN
    sum1,sum2=0,0
    for i in val1:
        for j in val1:
            if i == j: continue
            sum1 += MAP[i][j]

    for i in val2:
        for j in val2:
            if i == j: continue
            sum2 += MAP[i][j]

    MIN = min(MIN,abs(sum1-sum2))
    

if __name__ == "__main__":
    T = int(input())
    for TC in range(1,T+1):
        MIN = 999999999999
        N = int(input())
        MAP = [list(map(int,input().split())) for _ in range(N)]
        arr = [i for i in range(0,N)]

        for val in combinations(arr,N//2):
            val2 = [i for i in range(0,N) if i not in val]
            check(tmp1,tmp2,MAP)
            #print(val)
            
        print("#%d %d" %(TC,MIN))