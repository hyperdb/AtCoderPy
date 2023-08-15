# ABC-284 A - Sequence of Strings
# https://atcoder.jp/contests/abc284/tasks/abc284_a
#
def getInt():
    return int(input())


def getStringRow(N):
    return [input() for _ in range(N)]


def main():
    n = getInt()
    s = getStringRow(n)

    s.reverse()

    for w in s:
        print(w)


if __name__ == "__main__":
    main()
