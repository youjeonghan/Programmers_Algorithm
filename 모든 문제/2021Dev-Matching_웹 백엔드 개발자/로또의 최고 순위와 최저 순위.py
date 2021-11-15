# 레벨1


def solution(lottos, win_nums):
    cnt = 0
    zero_cnt = 0

    for i in lottos:
        if i == 0:
            zero_cnt += 1
            continue

        if i in win_nums:
            cnt += 1
    answer = [min(7 - (cnt + zero_cnt), 6), min(7 - cnt, 6)]
    return answer


if __name__ == "__main__":
    print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
