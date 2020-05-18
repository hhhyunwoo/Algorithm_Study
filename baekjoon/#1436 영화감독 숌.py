#1436 영화감독 숌
#비효율적이지만 2초라서 충분히 가능한듯!

n = int(input())

idx = 666
cnt = 1
while 1:
    if cnt == n:
        print(idx)
        break
    else:
        idx += 1
        if '666' in str(idx):
            cnt += 1
