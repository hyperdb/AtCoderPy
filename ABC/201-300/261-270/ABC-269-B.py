# ABC-269 B - Rectangle Detection
# https://atcoder.jp/contests/abc269/tasks/abc269_b
#
def getStringRow(N):
    return [input() for _ in range(N)]


def main():
    s = getStringRow(10)

    r = []
    for i in range(10):
        r.append(0 if s[i].find('#') == -1 else 1)

    sr = r.index(1)
    r.reverse()
    er = r.index(1)

    sc = s[sr].find('#')
    ec = s[sr].rfind('#')

    print(sr + 1, 10 - er)
    print(sc + 1, ec + 1)


if __name__ == "__main__":
    main()
