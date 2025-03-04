# ABC-394 B - cat
# https://atcoder.jp/contests/abc394/tasks/abc394_b
#
def getInt():
    return int(input())


def getStringRow(N):
    return [input() for _ in range(N)]


def main():
    N = getInt()
    S = getStringRow(N)

    print("".join(sorted(S, key=len)))


if __name__ == "__main__":
    main()
