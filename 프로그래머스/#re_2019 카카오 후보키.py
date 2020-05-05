#2019 카카오 후보키

'''
numpy.array에서
arr[:,3] 하면 열의 인덱스가 3인값을 추출함
'''

from itertools import combinations,permutations
import copy
import numpy as np

def solution(relation):
    arr = [i for i in range(0,len(relation[0]))]
    result = []
    for l in range(1,len(relation[0])+1):
        for val in combinations(arr,l):
            flag = 0
            #만약 val에 res가 존재한다면 안됨
            

            #val 가지고 유효성 검사    
            #tmp = copy.deepcopy(relation)
            #tmp2 = np.array(tmp)

            temp = []
            for r in relation:
                a = []
                for v in val:
                    a.append(r[v])
                temp.append(tuple(a))

            if len(set(temp)) == len(relation):
                result.append(val)
            '''
            for k in range(0,len(val)):
                for p in range(0,len(tmp)):
                    if list(tmp2[:,val[k]]).count(tmp[p][val[k]]) == 1:
                        #한개밖에없으면
                        tmp[p][val[k]] = -99999
                tmp3 = []    
                for p in range(0,len(tmp)):
                    if tmp[p][val[k]] != -99999:
                        tmp3.append(tmp[p])
                tmp = copy.deepcopy(tmp3)
                tmp2 = np.array(tmp)
                
            if not tmp3:
                result.append(val)'''
    answer = []
    #최소성
    for res in result:
        flag = 0
        for ans in answer: #부분집합 검사
            if set(ans).issubset(set(res)):
                flag = 1
                break
        if flag == 0:
            answer.append(res) 
    return len(answer)

if __name__ == "__main__":
    print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))





'''
#2019 카카오 후보키


#numpy.array에서
#arr[:,3] 하면 열의 인덱스가 3인값을 추출함


from itertools import combinations,permutations
import copy
import numpy as np

def solution(relation):
    arr = [i for i in range(0,len(relation[0]))]
    result = []
    for l in range(1,len(relation[0])+1):
        for val in combinations(arr,l):
            flag = 0
            #만약 val에 res가 존재한다면 안됨
            

            #val 가지고 유효성 검사    
            tmp = copy.deepcopy(relation)
            tmp2 = np.array(tmp)
            for k in range(0,len(val)):
                for p in range(0,len(tmp)):
                    if list(tmp2[:,val[k]]).count(tmp[p][val[k]]) == 1:
                        #한개밖에없으면
                        tmp[p][val[k]] = -99999
                tmp3 = []    
                for p in range(0,len(tmp)):
                    if tmp[p][val[k]] != -99999:
                        tmp3.append(tmp[p])
                tmp = copy.deepcopy(tmp3)
                tmp2 = np.array(tmp)
                
            if not tmp3:
                result.append(val)
    answer = []
    for res in result:
        flag = 0
        for ans in answer: #부분집합 검사
            if set(ans).issubset(set(res)):
                flag = 1
                break
        if flag == 0:
            answer.append(res) 
    return len(answer)

if __name__ == "__main__":

    print(solution([["b","2","a","a","b"],
                    ["b","2","7","1","b"],
                    ["1","0","a","a","8"],
                    ["7","5","a","a","9"],
                    ["3","0","a","f","9"]]))
'''