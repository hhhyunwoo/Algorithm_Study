#2477 swea 차량정비소

if __name__ == "__main__":
    T = int(input())
    for TC in range(1,T+1):
        N,M,K,A,B = map(int,input().split())
        A -= 1
        B -= 1
        a = list(map(int,input().split()))
        b = list(map(int,input().split()))
        t = list(map(int,input().split()))

        visited_A = [[0,0] for _ in range(len(a))]
        visited_B = [[0,0] for _ in range(len(b))]
        wait_A = list()
        wait_B = list()
        ans1 = list()
        ans2 = list()
        check = [0]*K

        while 1:
            if sum(check) == K:
                break

            #A에 도착
            for i in range(0,len(t)):
                if t[i] == 0: #접수처에 i가 도착
                    wait_A.append(i)
                    t[i] = -1
                elif t[i] > 0:
                    t[i] -= 1
            
            #A -> B
            #wait_B -> B 로도 체크해줘야함
            for i in range(0,len(visited_A)): #접수처 시간 줄여주기
                if visited_A[i][1] > 0:
                    visited_A[i][1] -= 1
                    if visited_A[i][1] == 0:#시간 다되면 접수처 비었다는 의미
                        wait_B.append(visited_A[i][0])
                        visited_A[i] = [0,0]

            #B->End
            for i in range(0,len(visited_B)): #정비소 시간 줄여주기
                if visited_B[i][1] > 0:
                    visited_B[i][1] -= 1

                    if visited_B[i][1] == 0:#시간 다되면
                        check[visited_B[i][0]] = 1
                        visited_B[i] = [0,0]
                        

            ##########################################여기까지 시간줄여주기            

            #T -> A
            wait_A.sort() #고객번호가 낮은 순서대로 우선접수
            for j in range(0,len(a)):
                if visited_A[j][1] == 0 and wait_A:#접수처에 빈자리 있으면
                    tmp = wait_A.pop(0)
                    visited_A[j] = [tmp,a[j]] #사람idx, 남은시간
                    if j == A:
                        ans1.append(tmp)
            
            for j in range(0,len(b)):
                if visited_B[j][1] == 0 and wait_B:#정비소에 빈자리 있으면
                    tmp = wait_B.pop(0)
                    visited_B[j] = [tmp,b[j]] #사람idx, 남은시간
                    if B == j:
                        ans2.append(tmp)

        answer = set(ans1).intersection(ans2)
        final = sum(answer) + len(answer)
        if final == 0:
            final = -1
        print("#%d %d" %(TC,final))

            
                    
''' 
1
2 2 6 1 2
3 2
4 2
0 0 1 2 3 4
'''