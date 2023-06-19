# ABC-247 B - Unique Nicknames
# https://atcoder.jp/contests/abc247/tasks/abc247_b
#
def getInt():
    return int(input())


def getStringListRow(N):
    return [list(input().split()) for _ in range(N)]


def chk(member, n):
    l = []
    for i in range(len(member)):
        if i == n:
            continue
        l.append(member[i][0])
        l.append(member[i][1])
    return False if member[n][0] in l and member[n][1] in l else True


def main():
    n = getInt()
    st = getStringListRow(n)

    r = True
    for i in range(n):
        if chk(st, i):
            continue
        r = False
    print('Yes' if r else 'No')


if __name__ == "__main__":
    main()
