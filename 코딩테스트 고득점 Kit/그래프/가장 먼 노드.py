# 레벨3     그래프      가장 먼 노드
# 26분 소요
# bfs 문제

from collections import deque, defaultdict


def solution(n, edge):
    dic = defaultdict(list)
    visit = [0] * (n + 1)

    for s, e in edge:
        dic[s].append(e)
        dic[e].append(s)

    que = deque()
    result = []
    que.append((1, 0))
    visit[1] = 1
    while que:
        t, t_len = que.popleft()
        for i in dic[t]:
            if visit[i] == 0:
                visit[i] = 1
                que.append((i, t_len + 1))
                if result and result[-1][1] < t_len + 1:
                    result = []
                result.append((i, t_len + 1))
    return len(result)


if __name__ == "__main__":
    print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
