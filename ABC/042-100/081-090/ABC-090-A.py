# ABC-090 A - Diagonal String
# https://atcoder.jp/contests/abc090/tasks/abc090_a
#
def getStringRow(N):
    return [input() for _ in range(N)]


def main():
    s = getStringRow(3)

    r = ''
    for i in range(3):
        r += s[i][i]
    print(r)


if __name__ == "__main__":
    main()
