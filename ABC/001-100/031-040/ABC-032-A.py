# ABC-032 A - 高橋君と青木君の好きな数
# https://atcoder.jp/contests/abc032/tasks/abc032_a
#
import math


def getInt():
    return int(input())


def main():
    a = getInt()
    b = getInt()
    n = getInt()

    c = math.lcm(a, b)

    print(c if c >= n else math.ceil(n / c) * c)


if __name__ == "__main__":
    main()
