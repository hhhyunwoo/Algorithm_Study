#2018 카카오 n진수 게임

result = ""
alp = ['A','B','C','D','E','F']
def change(n, val):
    global result
    if val == 0: return
    r = val%n
    val = val//n
    change(n,val)
    if r>=10:
        rr = r%10
        r = alp[rr]
    result += str(r)
    
def solution(n, t, m, p):
    global result
    answer = ''
    cnt = 0
    change_res = "00"
    val = 1
    idx = 1
    while cnt<t:
        result = ""
        change(n,val)
        change_res += result
        #len(change_res)
        if idx%m == 0:
            tmp = m
        else:
            tmp= idx%m
        if tmp == p:
            answer += change_res[idx]
            cnt += 1
        #if len(change_res) >=(m*(t-1)+p): break
        val += 1
        idx += 1
    
    return answer

if __name__ == "__main__":
    print(solution(16,16,2,2))

