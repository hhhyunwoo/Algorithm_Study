#2019 카카오 압축

'''
시간 너무 오래걸렸다.

사실 끝나는 조건만 생각해서
abc 에서 abc가 존재해서 이렇게 바로 끝나는지
아니면
abc 인데 abc가 존재하지 않아서 ab넣고 다시 c로 가는지

이 두가지 경우만 보면된다.

종료조건 다루는 로직이 잘 안되서 어려웠다...
'''

def solution(msg):
    answer = []
    alp = {i:chr(i+ord('A')-1) for i in range(1,27)}
    
    i = 0
    j = i+1
    while 1:
        cur = msg[i]
        j = i+1
        flag = 0
        next = cur
        while j<len(msg):#next 구하기
            if next in alp.values():
                i += 1
                next += msg[j]
            else: 
                alp[len(alp)+1] = next
                if len(next) > 1:
                    next = next[:len(next)-1]
                '''if j == len(msg)-1: #kao로 끝나는경우
                    flag = 1'''
                break

            
            j += 1

        if j == len(msg):#마지막
            if next not in alp.values():#없으면
                next = next[:-1]
            else:
                flag = 1

        '''if len(tmp) > 1 : 
            tmp = tmp[:len(tmp)-1]'''

        for key,value in alp.items():  
            if value == next:
                answer.append(key)
                break
        if flag == 1: break

    return answer

if __name__ == "__main__":
    print(solution('KAKAO'))

