# ABC-035 C - オセロ
# https://atcoder.jp/contests/abc035/tasks/abc035_c
#
def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    N, Q = getIntMap()
    lr = getIntListRow(Q)

    b = [0] + [0 for _ in range(N)]

    # いもす法
    for l, r in lr:
        b[l] += 1
        if r < N:
            b[r + 1] -= 1

    sum = 0
    r = ""
    for c in b[1:]:
        sum += c
        r += str(sum % 2)

    print(r)


if __name__ == "__main__":
    main()
