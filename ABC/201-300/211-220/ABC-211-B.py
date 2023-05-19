# ABC-211 B - Cycle Hit
# https://atcoder.jp/contests/abc211/tasks/abc211_b
#
def getStringRow(N):
    return [input() for _ in range(N)]


def main():
    s = getStringRow(4)

    print('Yes' if len(set(s)) == 4 else 'No')


if __name__ == "__main__":
    main()
