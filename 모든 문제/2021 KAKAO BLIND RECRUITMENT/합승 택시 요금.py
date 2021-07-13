from collections import defaultdict
import heapq as hq


def solution(n, s, a, b, fares):
    road = defaultdict(list)

    for s_node, t_node, fare in fares:
        road[s_node].append([fare, t_node])
        road[t_node].append([fare, s_node])

    def dijkstra(start, target):
        heap = []
        vertex = {i: float("inf") for i in range(1, n + 1)}
        vertex[start] = 0
        hq.heappush(heap, (0, start))

        while heap:
            w, node = hq.heappop(heap)
            if vertex[node] < w:
                continue

            for f, t_node in road[node]:
                if vertex[t_node] > vertex[node] + f:
                    vertex[t_node] = vertex[node] + f
                    hq.heappush(heap, (vertex[t_node], t_node))

        return vertex[target]

    result = float("inf")
    for i in range(1, n + 1):
        result = min(result, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))

    return result


if __name__ == "__main__":
    print(
        solution(
            6,
            4,
            5,
            6,
            [
                [2, 6, 6],
                [6, 3, 7],
                [4, 6, 7],
                [6, 5, 11],
                [2, 5, 12],
                [5, 3, 20],
                [2, 4, 8],
                [4, 3, 9],
            ],
        )
    )
