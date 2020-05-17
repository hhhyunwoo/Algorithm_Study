#2869 달팽이는 올라가고 싶다

import math
import sys
a,b,v = map(int,sys.stdin.readline().split())
if (v-a)%(a-b) == 0:
    print((v-a)//(a-b)+1)
else:
    print(math.ceil((v-a)/(a-b)+1))