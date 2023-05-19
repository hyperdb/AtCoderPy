# ABC-208 B - Factorial Yen Coin
# https://atcoder.jp/contests/abc208/tasks/abc208_b
#
import math


def getInt():
    return int(input())


def main():
    p = getInt()

    f = []
    i = 1
    while True:
        x = math.factorial(i)
        if x > p:
            break
        f.append(x)
        i += 1
    f.reverse()

    c = 0
    for i in f:
        if i > p:
            continue
        c += (p // i)
        p %= i
        if p == 0:
            break
    print(c)


if __name__ == "__main__":
    main()
