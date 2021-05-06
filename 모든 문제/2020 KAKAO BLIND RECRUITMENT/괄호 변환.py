# 2020 KAKAO BLIND RECRUITMENT  괄호 변환
def solution(p):
    def devide(st):
        open_cnt = 0
        close_cnt = 0
        u = v = ""
        idx = 0
        if st and st[idx] == "(":
            u += "("
            open_cnt += 1

        elif st and st[idx] == ")":
            u += ")"
            close_cnt += 1
        idx += 1

        while open_cnt != close_cnt:
            if idx < len(st) and st[idx] == "(":
                u += "("
                open_cnt += 1
            elif idx < len(st) and st[idx] == ")":
                u += ")"
                close_cnt += 1
            idx += 1

        if idx < len(st):
            v = st[idx:]

        return u, v

    def check(st):
        stack = []
        for i in st:
            if stack and i == ")" and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(i)
        if not stack:
            return 1
        else:
            return 0

    def reverse(st):
        result = ""
        for i in st:
            result += "(" if i == ")" else ")"
        return result

    def recursive(st):
        result = ""
        if st == "":
            return st

        u, v = devide(st)
        if check(u):
            result += u
            result += recursive(v)

        else:
            result = "("
            result += recursive(v) + ")"
            u = u[1:-1]
            result += reverse(u)
        return result

    return recursive(p)


if __name__ == "__main__":
    # print(solution("()))((()"))  # "()(())()"
    print(solution("()))((()"))
