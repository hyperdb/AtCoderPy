# ABC-340 A - Arithmetic Progression
# https://atcoder.jp/contests/abc340/tasks/abc340_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b, d = getIntMap()

    buf = []
    for i in range(a, b + 1, d):
        buf.append(str(i))

    print(" ".join(buf))


if __name__ == "__main__":
    main()
