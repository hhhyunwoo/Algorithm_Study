#1991 트리 순회

pree,inordere,poste = [],[],[]
def pre(arr,val):
    global res
    if val == '.': return
    pree.append(val)
    pre(arr,arr[val][0])
    inordere.append(val)
    pre(arr,arr[val][1])
    poste.append(val)
'''def inorder(arr,val):
    global res
    if val == '.': return
    inorder(arr,arr[val][0])
    res += str(val)
    inorder(arr,arr[val][1])

def post(arr,val):
    global res
    if val == '.': return
    post(arr,arr[val][0])
    post(arr,arr[val][1])
    res += str(val)'''

n = int(input())
arr = {chr(i+ord('A')):[] for i in range(0,n+1)}

for _ in range(n):
    val = list(map(str,input().split()))
    arr[val[0]] = [val[1],val[2]]

pre(arr,'A')
print(*pree)
print(*inordere)
print(*poste)
#print(arr)    
