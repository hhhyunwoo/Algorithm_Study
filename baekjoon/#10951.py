#10951 A+B-4
#얼마나 입력받는지 모르기때문에 고민했어야 했따.
import sys

for line in sys.stdin:#eof 까지 받는 것이다. 개행을 구분자로해서 입력받음
    a,b = map(int,line.split())
    print(a+b)
#이렇게 try except 사용해서도 가능함
#    try:
#        a, b = map(int,input().split())
#        print(a+b)
#    except:
#        break