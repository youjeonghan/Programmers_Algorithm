# 레벨2     연습 문제       올바른 괄호
# 2분 30초 소요


def solution(s):
    stack = []
    for i in s:
        if stack and stack[-1] == "(" and i == ")":
            stack.pop()
        else:
            stack.append(i)
    return False if stack else True


if __name__ == "__main__":
    print(solution(")()("))
