#2018 카카오 다트게임

'''
정규표현식 공부하기
'''

import math

def solution(dartResult):
    answer = 0
    darts = []
    tmp_list = []
    tmp = ""
    i = 0
    while i < len(dartResult):
        if i+1 < len(dartResult) and dartResult[i+1] == '0' and dartResult[i] == '1':
            tmp_list.append(10)
            i += 2
            continue

        tmp_list.append(dartResult[i]) 
        if (i+1) == len(dartResult) or dartResult[i+1].isdigit():
            darts.append(tmp_list)
            tmp_list = []
        i += 1
    cal = []
    for i in range(0, len(darts)):
        tmp = ""
        if darts[i][1] == 'S':
            tmp += str(pow(int(darts[i][0]), 1))
        elif darts[i][1] == 'D':
            tmp += str(pow(int(darts[i][0]), 2))
        elif darts[i][1] == 'T':
            tmp += str(pow(int(darts[i][0]), 3))

        if len(darts[i]) == 3:
            if darts[i][2] == '*':
                if i > 0:  # 첫번째가 아님
                    cal[i-1] += '*2'
                tmp += '*2'

            elif darts[i][2] == '#':
                tmp += '*(-1)'
        cal.append(tmp)

    for ca in cal:
        answer += eval(ca)
    return answer

if __name__ == "__main__":
    print(solution("1D2S#10S"))
