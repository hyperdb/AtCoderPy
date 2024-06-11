# ABC-089 B - Hina Arare
# https://atcoder.jp/contests/abc089/tasks/abc089_b
#
def getInt():
    return int(input())


def getStringList():
    return list(input().split())


def main():
    n = getInt()
    s = getStringList()

    print('Four' if 'Y' in s else 'Three')


if __name__ == "__main__":
    main()
