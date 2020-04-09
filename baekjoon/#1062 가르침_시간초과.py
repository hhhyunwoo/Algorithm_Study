#1062 가르침
#리스트 복사  arr = temp[:]
def dfs(cnt, visited):
    global alp
    global ans
    global arr
    if cnt >= alp:
        #단어 다 돌려보고, 개수를 ans 만들자
        read = 0
        for k in range(0,N):
            if arr[k] == "":
                read += 1
        ans = max(read,ans)
        return

    if ans >= K: return

    for i in range(0,26):
        if visited[i] == 0: #알파벳 안썼다면
            visited[i] = 1
            use = chr(i + ord('a'))
            temp = list()
            flag = 0
            for j in range(0,N):
                temp.append(arr[j])
                if use in arr[j]:
                    flag = 1 #만약에 바꿀값이 있으면
                    arr[j] = arr[j].replace(use,"")
            
            if flag == 1:
                dfs(cnt+1, visited)
            visited[i] = 0
            arr = temp[:]

'''3 7
antarctica
antahellotica
antacartica'''

if __name__ == "__main__":
    N, K = map(int, input().split())
    arr = list()
    for i in range(N):
        string = str(input())
        if len(string) == 8: #antactica 일때
            string = ""
        else:    
            string = string[4:]
            string = string[:len(string)-4]
        arr.append(string)
    #print(arr)
    for i in range(0,N):
        arr[i] = arr[i].replace("a","")
        arr[i] = arr[i].replace("c","")
        arr[i] = arr[i].replace("n","")
        arr[i] = arr[i].replace("t","")
        arr[i] = arr[i].replace("i","")
    
    visited = [0] * 26
    visited[ord('a')-ord('a')] = 1 #항상 들어가는 것
    visited[ord('c')-ord('a')] = 1
    visited[ord('n')-ord('a')] = 1
    visited[ord('t')-ord('a')] = 1
    visited[ord('i')-ord('a')] = 1
    

    #print(arr)
    alp = K-5
    ans = 0
    dfs(0, visited)
    print(ans)
