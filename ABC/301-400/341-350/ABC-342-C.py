# ABC-342 C - Many Replacement 
# https://atcoder.jp/contests/abc342/tasks/abc342_c
#
def getInt():
    return int(input())


def getString():
    return input()


def getStringListRow(N):
    return [list(input().split()) for _ in range(N)]


def main():
    n = getInt()
    s = getString()
    q = getInt()
    cd = getStringListRow(q)

    dic = {}
    a = ord('a')
    for c in range(26):
        dic[chr(a + c)] = chr(a + c)

    for c, d in cd:
        keys = [k for k, v in dic.items() if v == c]
        for k in keys:
            dic[k] = d

    r = []
    for c in s:
        r.append(dic[c])

    print("".join(r))


if __name__ == "__main__":
    main()
