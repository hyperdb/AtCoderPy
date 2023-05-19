# ABC-188 A - Slot
# https://atcoder.jp/contests/abc189/tasks/abc189_a
#
def getString():
    return input()


def main():
    s = getString()

    print('Won' if len(set(list(s))) == 1 else 'Lost')


if __name__ == "__main__":
    main()
