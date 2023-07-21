# ABC-270 A - 1-2-4 Test
# https://atcoder.jp/contests/abc270/tasks/abc270_a
#
def getIntMap():
    return map(int, input().split())


def q(n):
    r = []
    if n in [1, 2, 4]:
        r += [n]
    elif n == 3:
        r += [1, 2]
    elif n == 5:
        r += [1, 4]
    elif n == 6:
        r += [2, 4]
    elif n == 7:
        r += [1, 2, 4]
    return r


def main():
    a, b = getIntMap()

    print(sum(set(q(a) + q(b))))


if __name__ == "__main__":
    main()
