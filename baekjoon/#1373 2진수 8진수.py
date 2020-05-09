#1373 2진수 8진수

'''
oct 라는 함수가 있구나,,,,ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
'''
def change(q):
    q,r = divmod(q,8)
    if q == 0:
        return str(r)
    else:
        return change(q) + str(r)

def change2(val):
    val= val[::-1]
    res = ""
    while 1:
        if not val: break
        res += str(int(val[:3][::-1],2) & 7)
        val = val[3:]
    return res[::-1]
    
if __name__ =="__main__":
    print(oct(int(input(),2)[2:]))
    #num = input()
    #print(change2(num))