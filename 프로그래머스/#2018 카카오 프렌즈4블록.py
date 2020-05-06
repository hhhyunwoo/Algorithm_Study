#2018 카카오 프렌즈4블록

def check_boom(m,n,board):
    boom = []
    
    for y in range(m-1):
        for x in range(n-1):
            cur = board[y][x]
            if cur == -1: continue
            if board[y][x+1] == cur and board[y+1][x] == cur and board[y+1][x+1] == cur:
                boom.append((y,x))
    return boom

def elim(boom,board):
    for y,x in boom:
        board[y][x], board[y][x+1], board[y+1][x], board[y+1][x+1] = 0,0,0,0
    
def down(m,n,board):
    for x in range(0,n):
        tmp = []
        for y in range(m-1,-1,-1):
            if board[y][x] !=0:
                tmp.append(board[y][x])
        for y in range(m-1,-1,-1):
            if not tmp:
                cur = -1
            else:
                cur = tmp.pop(0)
            board[y][x] = cur

def solution(m, n, board):
    answer = 0
    boom = []
    for i in range(0,m):
        board[i] = list(board[i])
    while 1:
        boom = check_boom(m,n,board)
        if not boom: break
        elim(boom,board)
        down(m,n,board)

    count = 0
    for val in board:
        count += val.count(-1)
    return count

if __name__ == "__main__":
    print(solution(4,5,['CCBDE', 'AAADE', 'AAABF', 'CCBBF']))

