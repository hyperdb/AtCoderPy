# ABC-377 C - Avoid Knight Attack
# https://atcoder.jp/contests/abc377/tasks/abc377_c
#
def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def getKnight(x, y, size):
    buf = [(x, y)]
    jump = [
        [-1, -2],
        [1, -2],
        [2, -1],
        [2, 1],
        [1, 2],
        [-1, 2],
        [-2, 1],
        [-2, -1],
    ]
    for i, j in jump:
        nx = x + i
        ny = y + j
        if 0 <= nx < size and 0 <= ny < size:
            buf.append((nx, ny))

    return buf


def main():
    N, M = getIntMap()
    ab = getIntListRow(M)

    p = dict()
    for a, b in ab:
        q = [(key, None) for key in getKnight(a - 1, b - 1, N)]
        p.update(dict(q))

    print(N**2 - len(p))


if __name__ == "__main__":
    main()
