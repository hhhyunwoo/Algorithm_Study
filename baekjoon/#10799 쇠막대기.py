#10799 쇠막대기


import sys

flag = 0
stack = list()
comm = sys.stdin.readline()
laser = list()
stick=list()

for j in range(0,len(comm)-1):
    if comm[j] == ')': #레이져판별
        if comm[j-1] == '(': 
            laser.append((j-1,j))
        else:#레이져가 아니다
            start = stack.pop()
            stick.append((start,j))
    elif comm[j] == '(' and comm[j+1] == '(':
        stack.append(j)

sum = 0
for i in range(0,len(stick)):
    val = 0
    for j in range(0,len(laser)):
        if stick[i][0] < laser[j][0] and laser[j][0] < stick[i][1]:
            val += 1
    sum += val+1
print(sum)