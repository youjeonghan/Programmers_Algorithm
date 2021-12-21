# 레벨2     탐욕법(Greedy)      큰 수 만들기

from collections import deque


def solution(number, k):
    l = len(number)
    result = deque()
    for i in number:
        if not result or result[-1] >= i and l > k:
            result.append(i)
        elif result and result[-1] < i:
            while result and k and result[-1] < i:
                result.pop()
                k -= 1
            result.append(i)
        l -= 1

    return "".join(result)


if __name__ == "__main__":
    print(solution("1924", 2))
    print(solution("91", 1))
