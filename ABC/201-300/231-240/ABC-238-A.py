# ABC-238 A - Exponential or Quadratic
# https://atcoder.jp/contests/abc238/tasks/abc238_a
#
def getInt():
    return int(input())

def main():
    n = getInt()

    print('No' if 2 <= n <= 4 else 'Yes')


if __name__ == "__main__":
    main()