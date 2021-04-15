from collections import deque
from copy import deepcopy


def solution(s):
    li = deque(s)

    def check(t):
        stack = []
        while t:
            temp = t.popleft()
            if temp == "{" or temp == "(" or temp == "[":
                stack.append(temp)
            elif temp == "}" and stack and stack[-1] == "{":
                stack.pop()

            elif temp == ")" and stack and stack[-1] == "(":
                stack.pop()

            elif temp == "]" and stack and stack[-1] == "[":
                stack.pop()

            else:
                return 0
        if stack:
            return 0
        return 1

    answer = 0
    for _ in range(len(li)):
        answer += check(deepcopy(li))
        sym = li.popleft()
        li.append(sym)

    return answer


if __name__ == "__main__":
    print(solution("{"))
