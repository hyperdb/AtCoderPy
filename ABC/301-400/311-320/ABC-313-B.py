# ABC-313 B - Who is Saikyo?
# https://atcoder.jp/contests/abc313/tasks/abc313_b
#
def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]

def main():
    n, m = getIntMap()
    ab = getIntListRow(m)

    r = [0] + [0 for _ in range(n)]
    for a, b in ab:
        r[b] += 1

    w = []
    for i in range(1, len(r)):
        if r[i] == 0:
            w.append(i)

    print(w[0] if len(w) == 1 else -1)


if __name__ == "__main__":
    main()
