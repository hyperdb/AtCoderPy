# ABC-294 B - ASCII Art
# https://atcoder.jp/contests/abc294/tasks/abc294_b
#
def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def asc(c):
    return chr(ord('A') + c - 1)


def main():
    h, w = getIntMap()
    a = getIntListRow(h)

    for r in a:
        line = ''
        for c in r:
            line += '.' if c == 0 else asc(c)
        print(line)


if __name__ == "__main__":
    main()
