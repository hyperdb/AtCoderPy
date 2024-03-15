# ABC-339 B - Langton's Takahashi
# https://atcoder.jp/contests/abc339/tasks/abc339_b
#
def getIntMap():
    return map(int, input().split())


def main():
    h, w, n = getIntMap()
    d = 0  # 0 1 2 3
    x, y = (0, 0)

    map = [['.' for _ in range(w)] for _ in range(h)]

    for i in range(n):
        c = map[y][x]

        if c == '.':
            map[y][x] = '#'
            d = (d + 1) % 4
        else:
            map[y][x] = '.'
            d = (d - 1 + 4) % 4

        if d == 0:
            y = h - 1 if y == 0 else y - 1
        if d == 1:
            x = 0 if x == (w - 1) else x + 1
        if d == 2:
            y = 0 if y == (h - 1) else y + 1
        if d == 3:
            x = w - 1 if x == 0 else x - 1

    for r in map:
        print(''.join(r))


if __name__ == "__main__":
    main()
