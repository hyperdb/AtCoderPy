# ABC-277 B - Playing Cards Validation
# https://atcoder.jp/contests/abc277/tasks/abc277_b
#
def getInt():
    return int(input())


def getStringRow(N):
    return [input() for _ in range(N)]


def vc(c):
    if not c[0] in ['H', 'D', 'C', 'S']:
        return False
    if not c[1] in ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']:
        return False
    return True


def main():
    n = getInt()
    s = getStringRow(n)

    r = True
    if len(set(s)) == n:
        for c in s:
            if not vc(c):
                r = False
                break
    else:
        r = False
    print('Yes' if r else 'No')


if __name__ == "__main__":
    main()
