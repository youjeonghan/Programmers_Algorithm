# 레벨2     탐욕법(Greedy)      구명보트
# 다시
# 정답 보고 풀음


def solution(people, limit):
    people.sort()
    l, r = 0, len(people) - 1
    cnt = 0
    while l <= r:
        if people[l] + people[r] <= limit:
            l += 1
        r -= 1
        cnt += 1
    return cnt


if __name__ == "__main__":
    print(solution([70, 50, 80, 50], 100))
