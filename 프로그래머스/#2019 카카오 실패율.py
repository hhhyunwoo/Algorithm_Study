#2019 카카오 실패율

def solution(N, stages):
    answer = []
    arr = {}
    for j in range(1,N+1):
        a,b = 0,0
        for i in range(0,len(stages)):
            if stages[i] >= j:
                b +=1
            if stages[i] == j:
                a +=1
        if b == 0:
            arr[j] = 0.0
        else: arr[j] = a/float(b)
    
    
    arr = dict(sorted(arr.items(), key= lambda k: (k[1]), reverse=True))
    answer = list(arr.keys())
    
    
    return answer    

if __name__ == "__main__":
    print(solution(4,[4,4,4,4,4]))