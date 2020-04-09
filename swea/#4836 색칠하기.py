#4836 색칠하기

T = int(input())
for TC in range(1, T+1):
    N = int(input())
    red = list()
    blue = list()
    cnt = 0
    for i in range(N):
        x1,y1,x2,y2,color = map(int,input().split())
        for x in range(x1, x2+1):
            for y in range(y1,y2+1):
                if color == 1:#red
                    red.append((x,y))
                else:
                    blue.append((x,y))
    
    for i in range(len(red)):
        for j in range(len(blue)):
            if red[i][0] == blue[j][0] and red[i][1] == blue[j][1] :
                cnt += 1

    print("#%d %d" %(TC, cnt))