#1181 단어 정렬

n = int(input())
arr = sorted(set([str(input()) for _ in range(n)]),key=lambda k: (len(k),k))
for a in arr:
    print(a)