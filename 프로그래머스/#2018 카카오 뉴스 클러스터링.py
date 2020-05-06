#2018 카카오 뉴스 클러스터링

import copy

def solution(str1, str2):
    answer = 0
    str1_set,str2_set = [],[]
    for i in range(0,len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            tmp = str(str1[i].lower())+str(str1[i+1].lower())
            str1_set.append(tmp)
    for i in range(0,len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            tmp = str(str2[i].lower())+str(str2[i+1].lower())
            str2_set.append(tmp)

    union = copy.deepcopy(str1_set)
    union.extend(str2_set)
    inter = []
    #print(union)
    if len(str1_set) >= len(str2_set):
        for i in range(0,len(str1_set)):
            for j in range(0,len(str2_set)):
                if str1_set[i] == str2_set[j]:
                    inter.append(str2_set.pop(j))
                    break
    else:
        for i in range(0,len(str2_set)):
            for j in range(0,len(str1_set)):
                if str2_set[i] == str1_set[j]:
                    inter.append(str1_set.pop(j))
                    break
    #print(union, inter)
    if not union:
        answer = 1
    else:
        answer = len(inter)/float((len(union)-len(inter)))
    return int(answer * 65536)

if __name__ == "__main__":
    print(solution("handshake","shake hands"))

