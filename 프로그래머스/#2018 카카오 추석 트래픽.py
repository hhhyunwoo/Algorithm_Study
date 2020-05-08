#2018 카카오 추석 트래픽

'''
조금 복잡하게 푼 듯 하지만 그래도 로직을 생각해두고 푸니깐 깔끔하게 풀렸따

근데 start_list를 정렬안하고 접근해서 맨첨에 2개 틀렸었는데 정렬하니깐 잘 풀림!

로직은 이러하다


먼저 시간을 받은다음에 시작시간을 계산하고 start, end 리스트를 만든다

만들어진 리스트를 통해 비교한다

start ~ start + 1 구간과 
end ~ end +1 구간 이렇게 두개를 잡고 카운팅을 했다

먼저 구간안에 값이 들어와야 하기 때문에 구간을 잡고 2중 포문을 돌면서 완전 탐색을 하였다.
구간안에 있는지 비교하는 것은 지금 생각해보니 위에 처럼 기준을 잡고 그냥 단순 비교하면 될듯,,,
나는 start + 1 이라는 구간을 만들기 보다는 if 문으로 비교를 했다.
그래서 코드가 길어진 것 같다


와... 다른 풀이에서 그냥 h,m,s를 싹 초로 변환해서 계산한 사람이 있다. 그렇게 되면 내가 만든 compare 함수가 전혀 필요가 없다!! 

'''

import copy

def cmp_time(start,cmp): #start 가 크거나 같으면 1, 작으면 0
    #단순 시간 비교 h,m,s 각각 비교
    if start[0] > cmp[0]:
        return True
    elif start[0] < cmp[0]:
        return False
    else:
        if start[1] > cmp[1]:
            return True
        elif start[1] < cmp[1]:
            return False
        else:
            if start[2] >= cmp[2]:
                return True
            else:
                return False

def cmp_time2(start,cmp): #start 가 크거나 1, 작거나 같으면 0
    #단순 시간 비교 h,m,s 각각 비교
    if start[0] > cmp[0]:
        return True
    elif start[0] < cmp[0]:
        return False
    else:
        if start[1] > cmp[1]:
            return True
        elif start[1] < cmp[1]:
            return False
        else:
            if start[2] > cmp[2]:
                return True
            else:
                return False

def solution(lines):
    MAX = -99999999999
    traffics = []
    start_list = []
    for line in lines:
        tmp = list(map(str,line.split()))
        traffics.append(tmp[1:])
    for traffic in traffics:
        time = traffic[0]
        t = float(traffic[1].replace('s',''))
        h,m,s = int(time[:2]),int(time[3:5]),float(time[6:])

        if s-t+0.001 >= 0:
            start = [h,m,round(s-t+0.001,3)]
        else:
            if m-1>=0:
                start = [h,m-1,round(s-t+0.001+60.000,3)]
            else:
                start = [h-1,m-1+60,round(s-t+0.001+60.000,3)]
        end = [h,m,s]
        start_list.append([start,end])
    
    start_list = sorted(start_list,key=lambda k: (k[0][0],k[0][1],k[0][2]))
    
    for s in start_list: #모든 스타트 살핌
        cnt = 0
        for c in start_list:
            if cmp_time(s[0],c[0]) and cmp_time(c[1],s[0]):
                cnt +=1
            elif cmp_time(c[0],s[0]):
                tmp = copy.deepcopy(s[0])
                tmp[2] += 1 #1초 증가
                if cmp_time(c[0],tmp):
                    MAX = max(cnt,MAX)
                    break
                else:
                    cnt +=1
        MAX = max(cnt,MAX)

    for s in start_list: #모든 엔드 살핌
        cnt = 0
        for c in start_list:
            if cmp_time(s[1],c[0]) and cmp_time(c[1],s[1]):
                cnt +=1
            elif cmp_time(c[0],s[1]):
                tmp = copy.deepcopy(s[1])
                tmp[2] = round(tmp[2] + 1 - 0.001,3) #1초 증가
                if cmp_time2(c[0],tmp):
                    MAX = max(cnt,MAX)
                    break
                else:
                    cnt +=1
        MAX = max(cnt,MAX)
    return MAX

if __name__ == "__main__":
    print(solution(	["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]))

'''
[
'2016-09-15 01:00:04.001 2.0s',
'2016-09-15 01:00:07.000 2s'
]
'''