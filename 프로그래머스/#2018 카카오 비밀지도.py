#2018 카카오 비밀지도

'''
str_a.rjust(n,'0')
으로 하면 n크기 만큼 정렬되면서 0이 채워진다.
'''

def solution(n, arr1, arr2):
    answer = []
    print(str(bin(arr1[0])))
    for i in range(0,n):
        tmp1,tmp2 = str(bin(arr1[i]))[2:],str(bin(arr2[i]))[2:]
        if len(tmp1) <n:
            tmp = "0"*(n-len(tmp1))
            tmp1 = tmp+tmp1
        if len(tmp2) <n:
            tmp = "0"*(n-len(tmp2))
            tmp2 = tmp+tmp2    
        tmp3 = ""
        for j in range(0,n):
            if tmp1[j] == '0' and tmp2[j]=='0': #둘다 공백
                tmp3 +=' '
            else:
                tmp3 += '#'
        answer.append(tmp3)
    return answer

if __name__ == "__main__":
    print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))

