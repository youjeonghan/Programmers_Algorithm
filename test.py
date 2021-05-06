def reverse(st):
    result = ""
    for i in st:
        result += "(" if i == ")" else ")"
    return result


print(reverse(")("))