#4865 글자수
T = int(input())
for TC in range(1, T+1):
    arr1 = str(input())
    arr2 = str(input())

    arr1 = list(set(arr1))

    cntDic = {arr1[0] : 0}
    for i in range(1,len(arr1)):
        cntDic[arr1[i]] = 0

    for i in range(0,len(arr1)):
        for j in range(0,len(arr2)):
            if arr1[i] == arr2[j]:
                cntDic[arr1[i]] += 1
    
    MAX = -1
    for i in range(0,len(arr1)):
        if cntDic[arr1[i]] >= MAX:
            MAX = cntDic[arr1[i]]
    print("#%d %d" %(TC,MAX))