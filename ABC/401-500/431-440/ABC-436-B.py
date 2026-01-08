# ABC-436 B - Magic Square
# https://atcoder.jp/contests/abc436/tasks/abc436_b
#
def getInt():
    return int(input())


def main():
    N = getInt()
    a = [[-1 for _ in range(N)] for _ in range(N)]

    r = 0
    c = (N - 1) // 2
    k = 1

    a[r][c] = k

    for _ in range(N**2 - 1):
        # 新しい座標を計算
        r1 = (r - 1) % N
        r2 = (r + 1) % N
        c1 = (c + 1) % N

        if a[r1][c1] == -1:
            r = r1
            c = c1
            k += 1
        else:
            r = r2
            k += 1

        a[r][c] = k

    for row in a:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    main()
