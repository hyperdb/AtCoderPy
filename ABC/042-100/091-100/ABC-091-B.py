# ABC-091 B - Two Colors Card Game
# https://atcoder.jp/contests/abc091/tasks/abc091_b
#
def getInt():
    return int(input())


def getStringRow(N):
    return [input() for _ in range(N)]


def count(w, l):
    c = 0
    for s in l:
        if s == w:
            c += 1
    return c


def main():
    n = getInt()
    s = getStringRow(n)
    m = getInt()
    t = getStringRow(m)

    l = list(set(s))
    r = 0
    for w in l:
        c = count(w, s) - count(w, t)
        if r < c:
            r = c
    print(r if r >= 0 else 0)


if __name__ == "__main__":
    main()
