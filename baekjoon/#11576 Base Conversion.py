#11576 Base Conversion

def change(q,b):
    q,r = divmod(q,b)
    if q == 0:
        return str(r)
    else:
        return change(q,b) + " "+str(r)

if __name__ == "__main__":
    a,b = map(int,input().split())
    m = int(input())
    arr = list(map(int,input().split()))
    res = 0
    for i in range(0,m):
        res += arr[i]*pow(a,m-1-i)
    #res = oct(res)[2:]
    res = change(int(res),b)
    print(res)