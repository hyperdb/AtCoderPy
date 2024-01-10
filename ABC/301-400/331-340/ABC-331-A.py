# ABC-331 A - Tomorrow
# https://atcoder.jp/contests/abc331/tasks/abc331_a
#
def getIntMap():
    return map(int, input().split())


def main():
    mm, dd = getIntMap()
    y, m, d = getIntMap()

    d += 1
    if d > dd:
        d = 1
        m += 1
        if m > mm:
            m = 1
            y += 1

    print(y, m, d)


if __name__ == "__main__":
    main()
