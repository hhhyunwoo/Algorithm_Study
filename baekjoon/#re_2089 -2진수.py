#2089 -2진수
'''
개어렵다 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ

오바,,,
'''

def change(q):
    r = q%-2
    if r == -1 : r = 1
    q = (q-1)//-2

    if q == 0:
        return str(r)
    else:
        return change(q) + str(r)

print(change(int(input())))