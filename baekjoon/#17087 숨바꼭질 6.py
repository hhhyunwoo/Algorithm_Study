#17087 숨바꼭질 6

def gcd(a,b):
    while b:
        temp = a%b
        a = b
        b = temp
    return a

def lcm(a,b):
    c = gcd(a,b)
    return (a*b)//c

N, S = map(int,input().split())

arr= list(map(int,input().split()))
arr2 = list()
for i in range(0,len(arr)):
    arr2.append(abs(S-arr[i]))

a = arr2[0]

for i in range(1,len(arr)):
    a = gcd(a,arr2[i])

print(a)
