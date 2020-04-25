#1952 swea 수영장
def dfs(idx,sum):
    global MIN
    if idx >= 12:
        MIN = min(MIN,sum)
        return

    if plan[idx] == 0:
        dfs(idx+1,sum)
    else:    
        dfs(idx+1,sum+price[0]*plan[idx])
        dfs(idx+1,sum+price[1])
        dfs(idx+3,sum+price[2])


if __name__ == "__main__":
    global price
    global MIN
    T = int(input())
    for TC in range(1,T+1):
        price = list(map(int,input().split()))
        plan = list(map(int,input().split()))

        MIN = price[3] #1년짜리
        dfs(0,0)
        print("#%d %d" %(TC,MIN))
