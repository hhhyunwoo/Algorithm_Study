#2004 조합의 수

def check(n):
    val2,val5 = 0,0

    idx = 2
    while 1:
        if idx > n: break
        val2 += n//idx
        idx *=2
    idx = 5
    while 1:
        if idx >n: break
        val5 += n//idx
        idx *=5
    return [val2,val5]
if __name__ == "__main__":
    n,m = map(int,input().split())
    cnt_2,cnt_5 = 0,0
    res = check(n)
    cnt_2 += res[0]
    cnt_5 += res[1]

    res = check(n-m)
    cnt_2 -= res[0]
    cnt_5 -= res[1]

    res = check(m)
    cnt_2 -= res[0]
    cnt_5 -= res[1]

    print(min(cnt_2,cnt_5))