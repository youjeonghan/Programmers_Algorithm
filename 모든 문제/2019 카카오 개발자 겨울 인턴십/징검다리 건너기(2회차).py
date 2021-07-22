# 2019 카카오 개발자 겨울 인턴십    징검다리 건너기
# 2회차
# 다시 (효율성 통과 못함)
from collections import deque


def solution(stones, k):
    stones.append(float("inf"))
    result = []
    deq = deque()
    idx = len(stones) - 2  # 다음 추가해볼 idx
    for _ in range(k):
        deq.append(stones[idx])
        idx -= 1
    result.append(max(deq))

    while idx != -1:
        deq.popleft()
        deq.append(stones[idx])
        idx -= 1
        result.append(max(deq))

    # print(result)
    return min(result)


if __name__ == "__main__":
    print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
