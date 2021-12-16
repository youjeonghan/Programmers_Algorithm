# 레벨2     탐욕법(Greedy)      큰 수 만들기
# 시간초과 실패 다시풀기


from itertools import combinations


def solution(number, k):
    l = len(number)
    li = ["".join(i) for i in combinations(number, l - k)]
    li.sort()
    return li[-1]


if __name__ == "__main__":
    print(solution("1231234", 3))
