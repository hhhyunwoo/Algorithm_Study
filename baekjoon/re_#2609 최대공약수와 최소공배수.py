#2609 최대공약수와 최소공배수
def gdc(a,b):
    while b:
        tmp = a%b
        a = b
        b = tmp
    return a

def lcm(a,b):
    c = gdc(a,b)
    return (a*b)//c
A,B = map(int,input().split())

print(gdc(A,B))
print(lcm(A,B))
