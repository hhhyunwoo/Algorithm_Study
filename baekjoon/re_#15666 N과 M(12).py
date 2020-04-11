#15666 N과 M(12)

# permutation : 값들의 순서가 바뀌어도 상관없는 것. 즉, (1 2) 랑 (2 1)이랑 둘다 나온다!
# combination : permutation에서 순서가 바뀌면 똑같은 것들 Skip~~

# product : permutation에서 값들의 중복을 허용한다!
# combinations_with_replacment : Combination에서 값들의 중복을 허용한다!

from itertools import combinations, permutations,product, combinations_with_replacement

if __name__ == "__main__":
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))
    arr = sorted(arr)
    result = []
    for value in product(arr,repeat = M):
        print(value)
        if value not in result:
            result.append(value)
    print(result)
    '''ans = list()
    ansArr = list()
    visited = [0 for _ in range(10001)]
    dfs(0,ans,visited,-1)'''
    #ansArr = list(set(ansArr))
    #ansArr = sorted(ansArr)
    #for i in range(0,len(ansArr)):
    #    print(ansArr[i])