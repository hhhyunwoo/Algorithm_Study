
#1924 2007년
x, y = map(int,input().split())

Month = [31,28,31,30,31,30,31,31,30,31,30,31]
week = ['MON', 'TUE','WED', 'THU', 'FRI', 'SAT', 'SUN']
day = 0
for i in range(0,x-1):
    day += Month[i]
day += y
print(week[day % 7 - 1])