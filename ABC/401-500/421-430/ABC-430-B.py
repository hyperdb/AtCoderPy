# ABC-430 B - Count Subgrid
# https://atcoder.jp/contests/abc430/tasks/abc430_b
#
def getIntMap():
    return map(int, input().split())


def getStringRow(N):
    return [input() for _ in range(N)]


def cut_area(S, x, y, M):
    area = []
    for i in range(M):
        area.append(S[y + i][x : x + M])
    return area


def main():
    N, M = getIntMap()
    S = getStringRow(N)

    b = set()
    c = N - M + 1
    for y in range(c):
        for x in range(c):
            area = cut_area(S, x, y, M)
            b.add(tuple(area))

    print(len(b))


if __name__ == "__main__":
    main()
