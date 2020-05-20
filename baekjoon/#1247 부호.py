#1247 부호

for _ in range(3):
    n = int(input())
    res = sum([int(input()) for _ in range(n)])
    if res==0: i=0 
    elif res<0:i='-' 
    elif res>0:i='+'
    print(i)