
#4875 "미로"
# find 함수 제대로 익혀놓기! 찾고자하는 문자의 index를 반환할 수 있다.
#너무 어려웠다.
#맨첨에는 재귀 안쓰고 그냥 stack을 사용해서 풀려고 했는데 아!! 스택쓰고 visited 잘 썼다면 풀 수 있었을 수도?? 근데 너무 식이 복잡해져서 힘들었다.
#그래서 재귀함수 사용한 dfs를 이용했더니 너무 쉽게 풀렸따...
#저번에 풀어본 재귀 안쓴 dfs와 재귀 사용한 dfs를 한번 정리하자 진짜....
# dfs 문제중에 쉬운 문제일텐데 너무 힘들게 풀었다.. 반성하자.

def dfs(j,i):
    global ans
    if maze[j][i] == '3':
        ans = 1
        return
    visited.append((j,i))
    for dir in range(0,4):
        newj = j + dy[dir]
        newi = i + dx[dir]
        if 0<=newj<N and 0<=newi<N and maze[j][i] !='1' and (newj,newi) not in visited:
            dfs(newj,newi)
    #(maze[j][i] == '1' or maze[j][i] == '3') 

T = int(input())
for TC in range(1, T + 1):
    N = int(input())
    maze = list()
    for i in range(0,N): #지도 입력
        arr = str(input())
        maze.append(arr)
        if '2' in arr:
            j_start = i
        if '3' in arr:
            j_end = i
    i_start = maze[j_start].find('2')
    i_end = maze[j_end].find('3')

    visited = list()

    i_cur = i_start
    j_cur = j_start
    
    dy = [-1,1,0,0] #상하좌우
    dx = [0,0,-1,1]
    ans = 0
    dfs(j_start,i_start)

    if ans == 1:
        print("#%d %d" %(TC, 1))
    else:
        print("#%d %d" %(TC, 0))

    '''
    while 1:
        if i_cur == i_end and j_cur == j_end: 
            ans = 1
            break

        if flag == 1:#좌
            if i_cur - 1 <0 or maze[j_cur][i_cur-1] == '1' or (i_cur, j_cur) in visited:
                #좌표에서 벗어나거나, 벽으로 막혀있으면
                flag += 1
            else:
                visited.append((i_cur, j_cur))
                i_cur -= 1
                stk.append((i_cur, j_cur, flag))
        elif flag == 2:#상
            if j_cur - 1 <0 or maze[j_cur -1][i_cur] == '1' or (i_cur, j_cur) in visited:
                #좌표에서 벗어나거나, 벽으로 막혀있으면
                flag += 1
            else:
                visited.append((i_cur, j_cur))
                j_cur -= 1
                stk.append((i_cur, j_cur, flag))
                flag = 1# 다시 왼쪽부터 돌게하기
        elif flag == 3:#우
            if i_cur + 1 <0 or maze[j_cur][i_cur+1] == '1' or (i_cur, j_cur) in visited:
                #좌표에서 벗어나거나, 벽으로 막혀있으면
                flag += 1
            else:
                visited.append((i_cur, j_cur))
                i_cur += 1
                stk.append((i_cur, j_cur, flag))
                flag = 1
        elif flag == 4:#하
            if j_cur + 1 <0 or maze[j_cur + 1][i_cur] == '1' or (i_cur, j_cur) in visited:
                #좌표에서 벗어나거나, 벽으로 막혀있으면
                flag += 1
            else:
                visited.append((i_cur, j_cur))
                j_cur += 1
                stk.append((i_cur, j_cur, flag))
                flag = 1
        elif flag == 5: #한바퀴 다돌면 stack 에서 pop하고 뒤로가야함
            back = stk.pop()
            i_cur = back[0]
            j_cur = back[1]
            flag = back[2] + 1
            '''