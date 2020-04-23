#10820 문자열 분석
#isspace, islower 등의 메서드가 있다!
'''


'''
arr = list()
while 1:
    try:
        val = str(input())
        low,cap,num,blank = 0,0,0,0
        for i in range(0,len(val)):
            if val[i].isspace():
                blank += 1
            elif val[i].islower():
                low += 1
            elif val[i].isupper():
                cap += 1
            elif val[i].isdigit():
                num += 1

        answer = [low,cap,num,blank]
        print(*answer)
    except:
        break