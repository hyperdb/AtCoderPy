# ABC-123 A - Five Antennas
# https://atcoder.jp/contests/abc123/tasks/abc123_a
#
def getInt():
    return int(input())


def getIntRow(N):
    return [int(input()) for _ in range(N)]


def main():
    a = getIntRow(5)
    k = getInt()

    f = True
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if abs(a[j] - a[i]) > k:
                f = False
                break
    print('Yay!' if f else ':(')


if __name__ == "__main__":
    main()
