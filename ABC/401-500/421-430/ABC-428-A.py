# ABC-428 A - Grandma's Footsteps
# https://atcoder.jp/contests/abc428/tasks/abc428_a
#
def getIntMap():
    return map(int, input().split())


def main():
    S, A, B, X = getIntMap()

    d, m = divmod(X, A + B)

    r = (d * A * S) + (min(m, A) * S)

    print(r)


if __name__ == "__main__":
    main()
