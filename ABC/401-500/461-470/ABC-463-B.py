# ABC-463 B - Train Reservation
# https://atcoder.jp/contests/abc463/tasks/abc463_b
#
def getStringMap():
    return input().split()


def getStringRow(N):
    return [input() for _ in range(N)]


def main():
    N, X = getStringMap()
    S = getStringRow(int(N))

    x = ord(X) - ord("A")  # 列番号（0～）

    result = False
    for s in S:
        # 空席に当たればbreak
        if s[x] == "o":
            result = True
            break

    print("Yes" if result else "No")


if __name__ == "__main__":
    main()
