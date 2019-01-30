import random


def multiply(x, y):
    if x == 0:
        return 0

    a = x // 2
    b = y * 2
    prod = multiply(a, b)
    if x % 2 == 1:
        prod += y
    return prod


if __name__ == '__main__':
    x = 123
    y = 456

    res = multiply(x, y)
    print(f"{x} * {y} = {x * y} --> {x * y == res}")
    print("-" * 30)

    for _ in range(10):
        a = random.randint(0, 500000)
        b = random.randint(0, 500000)

        r = multiply(a, b)
        print(f"{a} * {b} = {a * b}--> {a * b == r}")
        print("-" * 30)
