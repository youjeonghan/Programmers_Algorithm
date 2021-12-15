# 레벨1     위클리 챌린지       최소직사각형


def solution(sizes):
    s_list = []
    l_list = []
    for i in sizes:
        i.sort(reverse=True)
        a, b = i
        s_list.append(a)
        l_list.append(b)
    return max(s_list) * max(l_list)


if __name__ == "__main__":
    print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
