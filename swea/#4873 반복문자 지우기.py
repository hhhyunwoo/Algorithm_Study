#4873 반복문자 지우기

T = int(input())

for TC in range(1, T + 1):
    string = str(input())
    i=0
    while 1:
        if i == len(string)-1:
            break
        if string[i] == string[i+1]:
            str1 = string[0:i]
            str2 = string[i+2:]
            string = str1 + str2
            #string = string.replace(string[i],"")
            i=0
        else:
            i += 1

    print("#%d %d" %(TC, len(string)))