# ABC-271 A - 484558
# https://atcoder.jp/contests/abc271/tasks/abc271_a
#
def getInt():
    return int(input())


def main():
    n = getInt()
    h = ['0', '1', '2', '3', '4', '5', '6',
         '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    print(h[n // 16] + h[n % 16])


if __name__ == "__main__":
    main()
