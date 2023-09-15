# ABC-306 A - Echo
# https://atcoder.jp/contests/abc306/tasks/abc306_a
#
def getInt():
    return int(input())


def getString():
    return input()


def main():
    n = getInt()
    s = list(getString())
    t = ''

    for c in s:
        t += (c * 2)

    print(t)


if __name__ == "__main__":
    main()
