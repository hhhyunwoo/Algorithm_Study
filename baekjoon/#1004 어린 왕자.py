#1004 어린 왕자
import math

def cal(x,y,cx,cy):
    return math.sqrt((cx-x)**2+(cy-y)**2)

if __name__== "__main__":
    t = int(input())
    for _ in range(t):
        x1,y1,x2,y2 = map(int,input().split())
        n=int(input())
        arr = []
        for _ in range(n):
            arr.append(list(map(int,input().split())))
        cnt = 0
        for a in arr:#시작점, 도착점이 각각 행성에 포함되는지
            if cal(x1,y1,a[0],a[1]) < a[2]: #시작점이 포함됨
                if cal(x2,y2,a[0],a[1]) < a[2]:#끝점도 포함
                    continue
                else:
                    cnt +=1
            else:
                if cal(x2,y2,a[0],a[1]) < a[2]:#끝점 포함
                    cnt +=1
                else:
                    continue
        print(cnt)