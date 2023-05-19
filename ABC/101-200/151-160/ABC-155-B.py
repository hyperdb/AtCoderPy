# ABC-155 B - Papers, Please
# https://atcoder.jp/contests/abc155/tasks/abc155_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def chk(n):
    if n % 2 != 0:
        return True
    if n % 3 == 0 or n % 5 == 0:
        return True
    return False


def main():
    n = getInt()
    a = getIntList()

    f = True
    for x in a:
        if chk(x):
            continue
        f = False
        break

    print('APPROVED' if f else 'DENIED')


if __name__ == "__main__":
    main()
