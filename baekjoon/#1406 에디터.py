#1406 에디터
import sys
stack_1= list(map(str,sys.stdin.readline().rstrip()))
m=int(sys.stdin.readline())

stack_2=[]

for _ in range(m):
    val = input()
    if val == 'L':
        if stack_1:
            stack_2.append(stack_1.pop())
    elif val == 'D':
        if stack_2:
            stack_1.append(stack_2.pop())
    elif val == 'B':
        if stack_1:
            stack_1.pop()
    else: #P $
        stack_1.append(val[2])
stack_1.extend(stack_2[::-1])
print(''.join(stack_1))