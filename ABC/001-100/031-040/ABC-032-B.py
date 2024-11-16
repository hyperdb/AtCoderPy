# ABC-032 B - 高橋君とパスワード
# https://atcoder.jp/contests/abc032/tasks/abc032_b
#
def getInt():
    return int(input())


def getString():
    return input()


def main():
    s = getString()
    k = getInt()
    l = len(s)

    d = set()
    for i in range(l - k + 1):
        d.add(s[i : i + k])

    print(len(d))


if __name__ == "__main__":
    main()
