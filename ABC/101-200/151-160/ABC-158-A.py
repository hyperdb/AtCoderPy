# ABC-158 A - Station and Bus
# https://atcoder.jp/contests/abc158/tasks/abc158_a
#
def getString():
    return input()


def main():
    l = list(getString())

    print('No' if len(set(l)) == 1 else 'Yes')


if __name__ == "__main__":
    main()
