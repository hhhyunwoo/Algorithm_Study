T = int(input())
for TC in range(1, T + 1):
    string = list(input().split())
    stk = list()
    ans = 0
    for i in range(len(string)-1):
        if string[i].isdigit():
            stk.append(string[i])
        else:
            try:
                b,a = int(stk.pop()), int(stk.pop())
                if string[i] == '+':
                    c = a + b
                elif string[i] == '-':
                    c = a - b
                elif string[i] == '*':
                    c = a * b
                elif string[i] == '/':  
                    c = a / b
                stk.append(str(c))

            except:
                ans = -1
    if ans == -1 or len(stk)>=2:
        print("#%d" %TC, "error")
    else :
        print("#%d %d" %(TC, int(stk.pop())))