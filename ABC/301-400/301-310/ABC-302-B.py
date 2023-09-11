# ABC-302 B - Find snuke
# https://atcoder.jp/contests/abc302/tasks/abc302_b
#
def getIntMap():
    return map(int, input().split())


def getStringListRow(N):
    return [list(input()) for _ in range(N)]


def chk(l, s):
    p = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]

    for i in range(len(p)):
        x = s[0]
        y = s[1]
        z = [s]
        for j in range(1, 5):
            x += p[i][0]
            y += p[i][1]
            z.append([x, y])

        t = ''
        for x, y in z:
            if 0 <= x < len(l[0]) and 0 <= y < len(l):
                t += l[y][x]
            else:
                break

        if t == 'snuke':
            return z
        else:
            continue
    return []


def main():
    h, w = getIntMap()
    s = getStringListRow(h)

    r = False
    for j in range(h):
        for i in range(w):
            if s[j][i] == 's':
                a = chk(s, [i, j])
                if len(a) > 0:
                    r = True
                    for x, y in a:
                        print('%d %d' % (y + 1, x + 1))
        if r:
            break


if __name__ == "__main__":
    main()
