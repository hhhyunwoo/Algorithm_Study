

def game(start,end):
    if end-start <= 1:  #base
        if (card[start][1] == card[end][1]) or (card[start][1] == 1 and card[end][1] == 3) or (card[start][1] == 2 and card[end][1] == 1)or (card[start][1] == 3 and card[end][1] == 2): #비기거나 start가 이김
            return (start,card[start][1])
        else :
            return (end, card[end][1])
    

    front = game(start,(start+end)//2)
    rear = game((start+end)//2+1,end)

    if (front[1] == rear[1]) or (front[1] == 1 and rear[1] == 3) or (front[1] == 2 and rear[1] == 1)or (front[1] == 3 and rear[1] == 2): #비기거나 front가 이김
        return front
    else :
        return rear

T = int(input())
for TC in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    card = list()
    for i in range(0,N):
        card.append((i,arr[i]))
    
    ans = game(0,N-1)

    print("#%d %d" %(TC, ans[0]+1))
