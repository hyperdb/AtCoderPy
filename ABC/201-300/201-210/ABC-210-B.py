# ABC-210 B - Bouzu Mekuri
# https://atcoder.jp/contests/abc210/tasks/abc210_b
#
def getInt():
    return int(input())


def getString():
    return input()


def main():
    n = getInt()
    s = getString()

    for i in range(n):
        if (s[i] == '1'):
            print('Takahashi' if i % 2 == 0 else 'Aoki')
            break


if __name__ == "__main__":
    main()
