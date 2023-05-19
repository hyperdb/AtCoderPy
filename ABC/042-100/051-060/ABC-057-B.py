# ABC-057 B - Checkpoints
# https://atcoder.jp/contests/abc057/tasks/abc057_b
#
def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    n, m = getIntMap()
    ab = getIntListRow(n)
    cd = getIntListRow(m)

    for i in range(len(ab)):
        x = 0
        y = 0
        for j in range(len(cd)):
            l = abs(ab[i][0] - cd[j][0]) + abs(ab[i][1] - cd[j][1])
            if j == 0:
                x = l
            elif l < x:
                x = l
                y = j
        print(y + 1)


if __name__ == "__main__":
    main()
