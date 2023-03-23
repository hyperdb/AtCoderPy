# ABC-179 B - Go to Jail
# https://atcoder.jp/contests/abc179/tasks/abc179_b
#
def getInt():
    return int(input())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    n = getInt()
    d = getIntListRow(n)

    z = 0
    for a in d:
        if len(set(a)) == 1:
            z += 1
        else:
            z = 0

        if z >= 3:
            break
    print('Yes' if z >= 3 else 'No')


if __name__ == "__main__":
    main()
