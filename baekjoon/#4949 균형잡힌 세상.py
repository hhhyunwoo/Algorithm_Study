#4949 균형잡힌 세상

while 1:
    val = str(input())
    if val == '.': break
    flag = 0
    stack = []
    for v in val:
        if v in ['(', '[']:
            stack.append(v)
        elif v == ')':
            if not stack:
                flag = 1
                print('no')
                break
            tmp = stack.pop()
            if tmp != '(':
                flag = 1
                print('no')
                break
        elif v == ']':
            if not stack:
                flag = 1
                print('no')
                break
            tmp = stack.pop()
            if tmp != '[':
                flag = 1
                print('no')
                break
    if flag ==0:
        if not stack:
            print('yes')
        else:
            print('no')
            #([ (([( [ ] ) ( ) (( ))] )) ])