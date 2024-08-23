# ABC-366 B - Vertical Writing
# https://atcoder.jp/contests/abc366/tasks/abc366_b
#
def getInt():
    return int(input())


def getStringRow(N):
    return [input() for _ in range(N)]


def main():
    N = getInt()
    S = getStringRow(N)
    S.reverse()

    for i in range(max([len(w) for w in S])):
        T = ""
        for s in S:
            T += s[i] if len(s) > i else "*"
        print(T.rstrip("*"))


if __name__ == "__main__":
    main()
