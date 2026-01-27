# ABC-068 C - Cat Snuke and a Voyage
# https://atcoder.jp/contests/abc068/tasks/arc079_a
#
def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    N, M = getIntMap()
    ab = getIntListRow(M)
    route = {}

    for a, b in ab:
        a -= 1
        b -= 1
        route.setdefault(a, set())
        route.setdefault(b, set())
        route[a].add(b)
        route[b].add(a)

    result = False
    for r in route.values():
        if 0 in r and N - 1 in r:
            result = True
            break

    print("POSSIBLE" if result else "IMPOSSIBLE")


if __name__ == "__main__":
    main()
