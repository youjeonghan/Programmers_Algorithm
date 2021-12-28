# 레벨2     Summer/Winter Coding(~2018)     영어 끝말잇기
# 16분 소요


from collections import defaultdict


def solution(n, words):
    result = [0, 0]
    dic = defaultdict(int)
    arr = [0] * n
    cur = 0
    for idx, i in enumerate(words):
        if idx != 0 and (words[idx - 1][-1] != i[0] or dic[i] != 0):
            return [cur + 1, arr[cur] + 1]
        dic[i] = 1
        arr[cur] += 1
        cur = (cur + 1) % n
    return result


if __name__ == "__main__":
    print(
        solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])
    )
