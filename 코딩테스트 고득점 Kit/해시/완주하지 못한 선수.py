# 레벨1     해시      완주하지 못한 선수
from collections import defaultdict


def solution(participant, completion):
    dic = defaultdict(lambda: 0)
    for i in completion:
        dic[i] += 1
    for i in participant:
        if dic[i] == 0:
            return i
        dic[i] -= 1


if __name__ == "__main__":
    print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
