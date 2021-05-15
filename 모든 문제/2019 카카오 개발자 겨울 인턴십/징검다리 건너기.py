# 2019 카카오 개발자 겨울 인턴십    징검다리 건너기
from collections import deque


def solution(stones, k):
    stones = [[i, k] for i in stones]
    stones.append([float("inf"), k])
    cnt = 0
    while 1:
        idx = len(stones) - 1
        min_value = float("inf")
        for i in stones:
            min_value = min(min_value, i[0])
        del_list = deque()
        while idx > 0:
            stones[idx][0] -= min_value
            if stones[idx][0] == 0:
                del_list.append(idx)
            idx -= 1

        cnt += min_value

        while del_list:
            t = del_list.popleft()
            stones[t + 1][1] -= 1
            if stones[t + 1][1] == 0:
                return cnt
            del stones[t]


if __name__ == "__main__":
    print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
