# ABC-033 C - 数式の書き換え
# https://atcoder.jp/contests/abc033/tasks/abc033_c
#
import math


def getString():
    return input()


def main():
    S = getString()

    a = S.split("+")
    c = 0
    for b in a:
        x = math.prod(map(int, b.split("*")))
        c += 1 if x > 0 else 0
    print(c)


if __name__ == "__main__":
    main()
