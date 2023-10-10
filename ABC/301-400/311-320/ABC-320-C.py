# ABC-320 C - Slot Strategy 2 (Easy)
# https://atcoder.jp/contests/abc320/tasks/abc320_c
#
def getInt():
    return int(input())


def getStringRow(N):
    return [list(input()) for _ in range(N)]


def pick(a, n, m):
    return a[n % m]


def main():
    m = getInt()
    s = getStringRow(3)

    r = []
    for x in range(m):
        for y in range(2 * m):
            if x == y:
                continue
            for z in range(3 * m):
                if x == z or y == z:
                    continue
                sx = pick(s[0], x, m)
                sy = pick(s[1], y, m)
                sz = pick(s[2], z, m)

                if sx == sy == sz:
                    r.append(max(x, y, z))

    print(min(r) if len(r) > 0 else -1)


if __name__ == "__main__":
    main()
