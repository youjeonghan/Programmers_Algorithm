from collections import defaultdict


def solution(dirs):
    dic = defaultdict(set)

    cnt = 0
    me = [0, 0]
    for i in dirs:

        # print(cnt, (me[0], me[1]), dic[(me[0], me[1])])

        if i not in dic[(me[0], me[1])]:
            if i == "U" and me[0] == 5:
                pass
            elif i == "D" and me[0] == -5:
                pass
            elif i == "R" and me[1] == 5:
                pass
            elif i == "L" and me[1] == -5:
                pass
            else:
                cnt += 1
                
        dic[(me[0], me[1])].add(i)

        if i == "U":
            v = "D"
            if me[0] != 5:
                me[0] += 1
        elif i == "D":
            v = "U"
            if me[0] != -5:
                me[0] -= 1
        elif i == "R":
            v = "L"
            if me[1] != 5:
                me[1] += 1
        elif i == "L":
            v = "R"
            if me[1] != -5:
                me[1] -= 1
        dic[(me[0], me[1])].add(v)
    return cnt


if __name__ == "__main__":
    print(solution("LLLLLLLLLUD"))
    # print(solution("LULLLLLLU"))
