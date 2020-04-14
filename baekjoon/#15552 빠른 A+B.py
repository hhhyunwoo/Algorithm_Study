#15552 빠른 A+B
import sys

N = int(sys.stdin.readline())

for _ in range(N):
    A,B = map(int,sys.stdin.readline().split())
    print(A+B)