#2018 카카오 방금그곡

'''
지하철에서 로직 생각하고 코드로 구현한 문제이다

재밌는 문재였다.

맨첨에는 단순하게 접근하였다가 #이 들어간 부분은 인덱스로 구별하지 못한다는 것을 알고 다시 한번 생각하게 되었다.

그래서 replace를 생각했지만 그것보단 그냥 임의의 값으로 바꿔주는 것이 이득이라고 생각했다.
왜냐면 우리가 찾는 값은 멜로디가 아니라 단순 멜로디 유무를 통해 타이틀을 얻는 것이기 때문이다.

그래서 멜로디 값들을 바꿔주었다.
나는 
1번 시간계산
2번 멜로디 변경 및 멜로디 계산
3번 계산한 멜로디들을 가지고 m이랑 비교
였다.

살짝 애매한게 만약 시간이 23:09 - 00:05 인 부분 이랑 23:59 - 23:58 인 경우를 처리하지 않았을때도 통과가 되었다. 
앗! 조건문에 00:00을 넘기지 않는다고 적혀있다,, ㅎㅎㅎ 뻘짓했네

맨첨에는 none을 출력하지 않고 계속 런타임 에러가 발생해서 당황하면서 뻘짓한 것 같다.

어쨌든 여기서 중요한 점은 시간계산하는 식 구하기와 멜로디를 변경할때 계산한 시간 값으로 하는 것인 것 같다

흥미로운 문제였다. 딱 적당한 난이도,, ㅎㅎ
'''

# C# D# F# G# A# -> 1,2,3,4,5
def change(val): #멜로디 #들어간것들 바꾸기
    tmp = ""
    i = 0
    while i<len(val):
        if i+1<len(val) and val[i+1] == '#':
            if val[i] == 'C':
                tmp += '1'
            elif val[i] == 'D':
                tmp += '2'
            elif val[i] == 'F':
                tmp += '3'
            elif val[i] == 'G':
                tmp += '4'
            elif val[i] == 'A':
                tmp += '5'
            i += 2
        else:
            tmp += val[i]
            i += 1
    return tmp
def solution(m, musicinfos):
    answer = ''
    m = change(m)
    musics = []
    mel_res = []
    res = []
    for val in musicinfos:
        musics.append(list(map(str,val.split(','))))
    #start,end,title,melody
    for music in musics:
        #시간계산
        start_h,start_m = int(music[0][:2]), int(music[0][3:])
        end_h,end_m = int(music[1][:2]), int(music[1][3:])
        if end_h < start_h or (end_h==start_h and start_m>end_m): #23 - 00
            time = (23-start_h+end_h)*60 + (60-start_m + end_m)
        else:
            time = (end_h-start_h)*60 + end_m - start_m
        #멜로디 변경 및 계산
        melody = change(music[3])
        if time>len(melody):
            tmp = melody*(time//len(melody)) + melody[:time%len(melody)]
        else:
            tmp = melody[:time]
        mel_res.append([tmp,time,music[2]])
        #멜로디,시간,제목 리턴

    #m 값 가지고 일치 여부 판단
    for mel in mel_res:
        if m in mel[0]:
            res.append(mel)
    
    res = sorted(res,key=lambda k: k[1],reverse=True)
    if not res:
        answer = "(None)"
    else:
        answer = res[0][2]

    return answer

if __name__ == "__main__":
    print(solution('ABC',['23:59,23:58,WORLD,C#D#F#G#A#', '13:00,13:05,WORLD2,ABCDEF']))

