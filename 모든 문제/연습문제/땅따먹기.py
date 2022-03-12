# 2레벨     연습문제        땅따먹기
import sys

sys.setrecursionlimit(10 ** 6)


def solution(land):
    land_len = len(land)
    for i in range(land_len - 1):
        sort_list = sorted(land[i], reverse=True)
        for idx in range(4):
            if land[i][idx] == sort_list[0]:
                land[i + 1][idx] += sort_list[1]
            else:
                land[i + 1][idx] += sort_list[0]
    return max(land[-1])


if __name__ == "__main__":
    print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))
