# ABC-377 B - Avoid Rook Attack
# https://atcoder.jp/contests/abc377/tasks/abc377_b
#
def getStringListRow(N):
    return [list(input()) for _ in range(N)]


def main():
    S = getStringListRow(8)

    r_cnt = 0
    for row in S:
        if "#" in row:
            continue
        r_cnt += 1

    C = [list(x) for x in zip(*S)]
    c_cnt = 0
    for col in C:
        if "#" in col:
            continue
        c_cnt += 1

    print(r_cnt * c_cnt)


if __name__ == "__main__":
    main()
