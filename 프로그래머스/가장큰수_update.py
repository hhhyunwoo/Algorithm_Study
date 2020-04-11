#숫자 범위 1<= <=1000
#마지막에 int하고 str해줘야 0001 이런값이 나올 수도 있음

def solution(numbers):
    numbers = list(map(str,numbers))
    numbers.sort(key = lambda x : x*3, reverse = True) 
    #주어지는 N값이 1~1000이니깐 3번 연속해서 반복해주면 소팅이 가능함!
    #인풋값이 주어질 때 범위를 잘 고려하면 푸는 방식 접근할 수 있을 듯. 
    #파이썬의 람다사용해서 소팅값 지정해주는 sort함수 익숙해지기! 
    answer = ''.join(numbers)
    #answer = ''.join(map(str,numbers))
    if answer[0] == '0':# or int(answer) == 0 :
        answer = str(int(answer))
        #값이 0이면에 대한 처리?
    return answer

if __name__ == "__main__":
    arr = list(map(str,input().split()))
    ans = solution(arr)
    print(ans)
    #print(string)
    #print(arr)

                    
#[6, 10, 2]