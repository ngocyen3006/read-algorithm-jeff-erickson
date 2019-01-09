import random


def fibonacciMultiply(x, y):
    hold = 0
    z = []
    for k in range(len(x) + len(y)):
        for i in range(0, k + 1):
            for j in range(0, k + 1):
                if i + j == k:
                    try:
                        hold += x[i] * y[j]
                    except IndexError:
                        continue

        z.append(hold % 10)
        hold = hold // 10
    return z


def makelist(n):
    l = list(map(int, reversed(str(n))))
    return l


def makeNumber(arr):
    n = 0
    for i in range(len(arr)):
        n += arr[i] * (10 ** i)
    return n


if __name__ == '__main__':
    x = 123
    y = 456

    x1 = makelist(x)
    y1 = makelist(y)

    res = fibonacciMultiply(x1, y1)
    res = makeNumber(res)
    print(f"{x} * {y} = {x * y} --> {x * y == res}")
    print("-" * 30)

    for _ in range(10):
        a = random.randint(0, 50000)
        b = random.randint(0, 50000)

        a1 = makelist(a)
        b1 = makelist(b)

        r = fibonacciMultiply(a1, b1)
        r = makeNumber(r)
        print(f"{a} * {b} = {a * b} --> {a * b == r}")
        print("-" * 30)
