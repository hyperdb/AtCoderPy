# ABC-335 C - Loong Tracking
# https://atcoder.jp/contests/abc335/tasks/abc335_c
#
def getIntMap():
    return map(int, input().split())


def getStringListRow(N):
    return [list(input().split()) for _ in range(N)]


def main():
    n, q = getIntMap()
    query = getStringListRow(q)

    d = [[i + 1, 0] for i in range(n)]
    d.reverse()

    for t, c in query:
        if t == '1':
            h = [d[-1][0], d[-1][1]]
            if c == 'R':
                h[0] += 1
            elif c == 'L':
                h[0] -=  1
            elif c == 'U':
                h[1] += 1
            elif c == 'D':
                h[1] -= 1
            d.append(h)
        else:
            print(" ".join(map(str, d[-1 * int(c)])))


if __name__ == "__main__":
    main()
