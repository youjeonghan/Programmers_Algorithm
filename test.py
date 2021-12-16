def oddNumbers(l, r):
    return [i for i in range(l, r + 1) if i % 2 == 1]


if __name__ == "__main__":
    print(oddNumbers(2, 5))
