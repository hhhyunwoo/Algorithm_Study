#15663 N과 M(9)
#visited 를 바꿔야함
#왜???
#왜 flag 초기화 시켜주면 돌아가지;?????

def dfs(cnt,ans,visited,flag):
    global ansArr
    if cnt == M:
        #ansArr.append(' '.join(map(str,ans)))
        print(' '.join(map(str,ans)))
        return
    flag = 0#####################
    for i in range(0,len(arr)):
        if visited[i] == 0 and flag != arr[i]:
            ans.append(arr[i])
            flag = arr[i]
            visited[i] = 1
            dfs(cnt+1, ans,visited,flag)
            ans.pop()
            visited[i] = 0

if __name__ == "__main__":
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))
    arr = sorted(arr)   
    ans = list()
    ansArr = list()
    visited = [0 for _ in range(10001)]
    dfs(0,ans,visited,-1)
    #ansArr = list(set(ansArr))
    #ansArr = sorted(ansArr)
    #for i in range(0,len(ansArr)):
    #    print(ansArr[i])