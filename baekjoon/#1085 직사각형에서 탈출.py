#1085 직사각형에서 탈출

x,y,w,h = map(int,input().split())
print(min(min(w-x,h-y),min(x,y)))
