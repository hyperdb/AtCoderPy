# ABC-412 A - Task Failed Successfully
# https://atcoder.jp/contests/abc412/tasks/abc412_a
#
def getInt():
    return int(input())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    N = getInt()
    AB = getIntListRow(N)

    ans = 0
    for a, b in AB:
        if a < b:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
