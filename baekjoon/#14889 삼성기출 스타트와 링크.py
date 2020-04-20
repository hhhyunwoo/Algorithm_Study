#14889 삼성기출 스타트와 링크

from itertools import combinations

if __name__=="__main__":
    N = int(input())

    MAP = [list(map(int,input().split())) for _ in range(N)]
    arr = [i for i in range(0,N)]
    answer = 99999999999

    for val in combinations(arr,N//2):
        visited = [0 for _ in range(N)]
        start = 0
        link = 0
        arr_link = list()
        
        for i in val: #start
            visited[i] = 1
            for j in val:
                if i!=j:
                    start += MAP[i][j]
        
        for i in range(0,N):
            if visited[i] == 0:
                arr_link.append(i)
        
        for i in arr_link:
            for j in arr_link:
                if i!=j:
                    link+= MAP[i][j]

        answer = min(answer, abs(start-link))
    
    print(answer)

