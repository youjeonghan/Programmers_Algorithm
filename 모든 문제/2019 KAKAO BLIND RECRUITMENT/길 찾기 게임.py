# 3레벨     2019 KAKAO BLIND RECRUITMENT        길 찾기 게임
# 다시 풀기

from collections import defaultdict, deque


def solution(nodeinfo):
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)
    nodeinfo = sorted(nodeinfo, key=lambda x: (-x[1], x[0]))
    z = list(zip(*nodeinfo))
    max_x, max_y = max(z[0]), max(z[1])
    gp = [[0] * max_x for _ in range(max_y)]
    dic = defaultdict(lambda: {"L": 0, "R": 0})
    level_dic = defaultdict(int)

    deq = deque([nodeinfo[0]])
    idx = 1
    while deq:
        nx, ny, n = deq.popleft()
        if level_dic[ny] == 0:
            level_dic[ny] = nodeinfo[idx][2]
        elif level_dic[ny] > nodeinfo[idx][2]:
            break

        while nodeinfo[idx][2] == level_dic[ny] and dic[n]["R"] == 0:
            if idx >= len(nodeinfo):
                break
            if dic[n]["L"] == 0 and nx > nodeinfo[idx][0]:
                dic[n]["L"] = nodeinfo[idx][2]
                deq.append(nodeinfo[idx])
                idx += 1
            elif dic[n]["R"] == 0 and nx < nodeinfo[idx][1]:
                dic[n]["R"] = nodeinfo[idx][1]
                deq.append(nodeinfo[idx])
                idx += 1
                break
        if idx >= len(nodeinfo):
            break


if __name__ == "__main__":
    print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))
