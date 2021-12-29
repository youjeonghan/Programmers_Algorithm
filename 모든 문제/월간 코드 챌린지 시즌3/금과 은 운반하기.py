# 레벨3     월간 코드 챌린지 시즌3      금과 은 운반하기
# 이분탐색 알아차리고 금, 은 조절 어떻게 할지에서 막혀서 답봄
# 다시


def solution(a, b, g, s, w, t):
    l = 1
    r = 10 ** 9 * 10 ** 5 * 2 * 2
    answer = float("inf")
    while l <= r:
        mid = (l + r) // 2
        gold = silver = total = 0

        for i in range(len(g)):
            deliver_cnt = mid // (t[i] * 2) + 1 if mid % (t[i] * 2) >= t[i] else mid // (t[i] * 2)
            gold += g[i] if deliver_cnt * w[i] > g[i] else deliver_cnt * w[i]
            silver += s[i] if deliver_cnt * w[i] > s[i] else deliver_cnt * w[i]
            total += g[i] + s[i] if deliver_cnt * w[i] > g[i] + s[i] else deliver_cnt * w[i]
        if gold >= a and silver >= b and total >= a + b:
            answer = min(answer, mid)
            r = mid - 1
        else:
            l = mid + 1
    return answer


if __name__ == "__main__":
    print(solution(90, 500, [70, 70, 0], [0, 0, 500], [100, 100, 2], [4, 8, 1]))
