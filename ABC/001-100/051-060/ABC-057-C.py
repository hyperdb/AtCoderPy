# ABC-057 C - Digits in Multiplication
# https://atcoder.jp/contests/abc057/tasks/abc057_c
#
import math


def getInt():
    return int(input())


def digit(n):
    return len(str(n))


def main():
    n = getInt()

    # n = 1 なら 1
    if n == 1:
        print(1)

    # x * x = nの範囲まで精査
    # 解の初期値はnの桁数
    else:
        x = math.sqrt(n)
        r = digit(n)
        a = 2
        while a <= x:
            if n % a == 0:
                b = n // a
                c = max([digit(a), digit(b)])
                r = c if c < r else r
            a += 1
        print(r)


if __name__ == "__main__":
    main()
