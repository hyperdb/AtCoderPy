# ABC-373 A - September
# https://atcoder.jp/contests/abc373/tasks/abc373_a
#
def getStringRow(N):
    return [input() for _ in range(N)]


def main():
    S = getStringRow(12)

    c = 0
    for i in range(12):
        if len(S[i]) - i == 1:
            c += 1

    print(c)


if __name__ == "__main__":
    main()
