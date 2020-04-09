#1992 쿼드트리
#행렬 
#mat = [input() for _ in range(n)]
#image = [list(r().strip()) for _ in range(N)]
#이렇게 바로 입력받을 수 있음

#대충 나오긴 했는데 내가 Basis Case를 제대로 못준 것 같다. 그래서 괄호가 이상하게 나와서 꽤 전전긍긍했던,,,

def dfs(y,x,N):
    global ans
    
    if N == 1:
        ans += MAP[y][x]
        return
    
    flag = True
    for i in range(y,N+y):
        for j in range(x,N+x):
            if MAP[i][j] != MAP[y][x]:
                flag = False
                break
    
    if flag: 
        ans += MAP[i][j]
    else:
        ans += "("
        dfs(y,x,N//2) #1
        dfs(y,x+N//2,N//2) #2
        dfs(y+N//2,x,N//2) #3
        dfs(y+N//2,x+N//2,N//2) #4
        ans += ")"
    

N = int(input())
MAP = [['0' for _ in range(N)] for _ in range(N)]

for i in range(0,N):
    string = str(input())
    for j in range(0,N):
        if string[j] == '1':
            MAP[i][j] = '1'
ans = ""

dfs(0,0,N)
print(ans)