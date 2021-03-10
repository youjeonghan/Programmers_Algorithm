from collections import deque


def solution(priorities, location):
    li = deque()
    for i in range(len(priorities)):
        li.append([priorities[i], i])

    priorities.sort()

    idx = 0
    while priorities:
        if priorities[-1] == li[0][0]:
            idx += 1
            if li[0][1] == location:
                answer = idx
                break
            li.popleft()
            priorities.pop()
        else:
            li.append(li.popleft())

    # li.sorted(key=lambda x: (-x[0], x[1]))
    # print(li)
    # for i in range(len(li)):
    #     if location == li[i][1]:
    #         answer = i + 1
    #         break
    return answer


priorities = [2, 1, 3, 2]
location = 2

# priorities = [1, 1, 9, 1, 1, 1]
# location = 0
print(solution(priorities, location))