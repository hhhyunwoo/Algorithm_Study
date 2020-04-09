#4864 문자열 비교


T = int(input())
for TC in range(1, T+1):
    str1 = str(input())
    str2 = str(input())

    if str1 in str2:
        print("#%d %d" %(TC,1))
    else :
        print("#%d %d" %(TC,0))