#11653 소인수분해

if __name__ == "__main__":
    a = int(input())

    while a != 1:
        i = 2
        while 1:
            if a % i == 0:
                print(i)
                a //= i
                break
            else:
                i += 1
        