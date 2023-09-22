# ABC-310 B - Strictly Superior
# https://atcoder.jp/contests/abc310/tasks/abc310_b
#
def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    n, m = getIntMap()
    pl = getIntListRow(n)

    fl = [pl[i][2:] for i in range(n)]  # pick function list

    r = False
    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            pi = pl[i][0]
            pj = pl[j][0]
            fi = set(fl[i])
            fj = set(fl[j])

            if pi < pj:
                continue
            if not fi.issubset(fj):
                continue
            if pi > pj:
                r = True
                break
            elif len(fj - fi) > 0:
                r = True
                break
        if r:
            break
    print('Yes' if r else 'No')


if __name__ == "__main__":
    main()
