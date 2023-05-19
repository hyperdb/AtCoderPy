# ABC-109 B - Shiritori
# https://atcoder.jp/contests/abc109/tasks/abc109_b
#
def getInt():
    return int(input())


def getStringRow(N):
    return [input() for _ in range(N)]


def main():
    n = getInt()
    w = getStringRow(n)

    r = True
    if len(w) != len(set(w)):
        r = False
    else:
        for i in range(1, n):
            if w[i - 1][-1] != w[i][0]:
                r = False
    print('Yes' if r else 'No')


if __name__ == "__main__":
    main()
