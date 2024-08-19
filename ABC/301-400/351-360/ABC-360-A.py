# ABC-360 A - A Healthy Breakfast
# https://atcoder.jp/contests/abc360/tasks/abc360_a
#
def getString():
    return input()


def main():
    S = getString()

    print('Yes' if S.find('R') < S.find('M') else 'No')


if __name__ == "__main__":
    main()
