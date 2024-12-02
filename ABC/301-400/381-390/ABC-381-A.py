# ABC-308 A - 11/22 String
# https://atcoder.jp/contests/abc381/tasks/abc381_a
#
def getInt():
    return int(input())


def getString():
    return input()


def main():
    N = getInt()
    S = getString()

    r = False

    t = S.split("/")
    if len(t) == 2:
        s1, s2 = t

        if s1 == s2 == "":
            r = True
        elif int(s1) * 2 == int(s2):
            r = True

    print("Yes" if r else "No")


if __name__ == "__main__":
    main()
