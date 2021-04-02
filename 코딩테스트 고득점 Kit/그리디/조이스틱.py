def solution(name):
    string = name
    list_str = []
    ch_cnt = 0
    for i in range(len(string)):
        list_str.append("A")

    # 알파벳 최소 변환 횟수
    alphabet_min = 0
    for i in range(len(string)):
        if string[i] != "A":
            ch_cnt += 1
            up = ord(string[i]) - ord("A")
            down = ord("Z") - ord(string[i]) + 1
            alphabet_min = alphabet_min + (up if up < down else down)

    # 커서 최소 이동 횟수
    cursor_min = 0
    idx = 0
    temp_list = list(string[:])
    if temp_list[0] != "A":
        temp_list[0] = "A"
        ch_cnt -= 1
    while 1:
        if ch_cnt == 0:
            break

        l = r = 1
        while temp_list[idx - l] == "A":
            l += 1
        while temp_list[idx + r] == "A":
            r += 1

        if l == r:  # 둘 다 같을경우 그이후 빨리 끝나는쪽을 선택
            pl, pr = l + 1, r + 1
            while temp_list[idx - pl] != "A":
                pl += 1
            while temp_list[idx + pr] != "A":
                pr += 1
            cursor_min += l if pl < pr else r
            idx += -l if pl < pr else r

        else:
            cursor_min += l if l < r else r
            idx += -l if l < r else r

        ch_cnt -= 1

    return alphabet_min + cursor_min


if __name__ == "__main__":
    print(solution("BBBBAAB"))  # 10
    print(solution("JEROEN"))  # 56