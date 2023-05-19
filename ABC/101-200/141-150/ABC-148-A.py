# ABC-148 A - Round One
# https://atcoder.jp/contests/abc148/tasks/abc148_a
#
def getIntRow(N):
    return [int(input()) for _ in range(N)]


def main():
    n = getIntRow(2)
    m = [i for i in [1, 2, 3] if i not in n]

    print(sum(m))


if __name__ == "__main__":
    main()
