import random


def peasantMul(x, y):
    prod = 0
    while x > 0:
        if x % 2 == 1:
            prod += y
        x = x // 2
        y += y
    return prod


if __name__ == '__main__':
    x = 123
    y = 456

    res = peasantMul(x, y)
    print(f"{x} * {y} = {x * y} --> {x * y == res}")
    print("-" * 30)

    for _ in range(10):
        a = random.randint(0, 50000)
        b = random.randint(0, 50000)

        r = peasantMul(a, b)
        print(f"{a} * {b} = {a * b}--> {a * b == r}")
        print("-" * 30)
