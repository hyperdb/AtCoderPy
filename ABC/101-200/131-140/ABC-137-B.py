# ABC-137 B - One Clue
# https://atcoder.jp/contests/abc137/tasks/abc137_b
#
def getIntMap():
    return map(int, input().split())


def main():
    k, x = getIntMap()

    if k == 1:
        print(x)
    else:
        a = x - k + 1
        a = a if a > -1000000 else -1000000
        b = x + k - 1
        b = b if b < 1000000 else 1000000

        c = []
        for i in range(a, b + 1):
            c.append(str(i))
        print(' '.join(c))


if __name__ == "__main__":
    main()
