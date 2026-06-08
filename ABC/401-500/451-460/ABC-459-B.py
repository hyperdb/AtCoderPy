# ABC-459 B - 459
# https://atcoder.jp/contests/abc459/tasks/abc459_b
#
def getInt():
    return int(input())


def getStringList():
    return list(input().split())


def getCode(s):
    code = [
        2,
        2,
        2,  # a, b, c
        3,
        3,
        3,  # d, e, f
        4,
        4,
        4,  # g, h, i
        5,
        5,
        5,  # j, k, l
        6,
        6,
        6,  # m, n, o
        7,
        7,
        7,
        7,  # p, q, r, s
        8,
        8,
        8,  # t, u, v
        9,
        9,
        9,
        9,  # w, x, y, z
    ]
    return code[ord(s[0]) - ord("a")]


def main():
    N = getInt()
    S = getStringList()

    for s in S:
        print(getCode(s), end="")


if __name__ == "__main__":
    main()
