#2018 카카오 파일명 정렬

def solution(files):
    answer = []
    file_list = []
    for file in files:
        idx = 0
        tail = ""
        tmp = ""
        flag = 0
        while idx<len(file):
            if flag == 1 and not file[idx].isdigit():#숫자 끝나면
                break
            elif flag == 0 and file[idx].isdigit():
                head = tmp
                tmp = ""
                flag = 1
            else:
                tmp += file[idx]
                idx += 1
        if tail == "":
            number = tmp
        file_list.append((head,int(number),file))
    file_list = sorted(file_list,key=lambda k: (k[0].lower(), k[1]))
    for file in file_list:
        answer.append(file[2])

    return answer

if __name__ == "__main__":
    print(solution(["F-5 Freedom Fighter", "B-50 Superfortress","A-10 Thunderbolt II", "F-14 Tomcat"]))