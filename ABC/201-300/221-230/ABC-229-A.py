# ABC-229 A - First Grid
# https://atcoder.jp/contests/abc229/tasks/abc229_a
#
def getStringRow(N):
    return [input() for _ in range(N)]


def main():
    s = getStringRow(2)

    s.sort()

    print('No' if s[0] == '#.' and s[1] == '.#' else 'Yes')


if __name__ == "__main__":
    main()
