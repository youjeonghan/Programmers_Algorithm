from collections import Counter


def solution(N, stages):
    answer = [[i, 0] for i in range(1, N + 1)]

    count = Counter(stages)
    all_people = len(stages)

    for i in range(N):
        if answer[i][0] == 0:
            answer[i][1] = 0

        elif all_people != 0:
            answer[i][1] = count[answer[i][0]] / all_people
            all_people -= count[answer[i][0]]

    answer.sort(key=lambda x: -x[1])

    return [x[0] for x in answer]


# N = 5
# stages = [2, 1, 2, 6, 2, 4, 3, 3]

N = 4
stages = [4, 4, 4, 4, 4]

print(solution(N, stages))