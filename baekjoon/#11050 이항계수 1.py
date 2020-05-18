#11050 이항계수 1
import math

n,k = map(int,input().split())

print(math.factorial(n) // (math.factorial(n-k)*math.factorial(k)))
        