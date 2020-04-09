#4866 괄호검사


T = int(input())

for TC in range(1, T + 1):
    stk = []
    ans = 1
    String = str(input())
    strArr = list(String)
    for i in range(0, len(strArr)):
        if strArr[i] == '(' or strArr[i] == '{':
            stk.append(strArr[i])
        elif strArr[i] == ')' or strArr[i] == '}':
            if not stk:
                ans = 0
                break
            P = stk.pop()
            if strArr[i] == ')' and P != '(':
                ans = 0
            elif strArr[i] == '}' and P != '{':
                ans = 0
    if stk:
        ans = 0
    print("#%d %d" %(TC, ans))