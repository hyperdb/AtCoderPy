# ABC-414 B - String Too Long
# https://atcoder.jp/contests/abc414/tasks/abc414_b
#
def getInt():
    return int(input())


def getStringListRow(N):
    return [list(input().split()) for _ in range(N)]


def main():
    N = getInt()
    cl = getStringListRow(N)

    str = ""
    size = 0
    for c, l in cl:
        size += int(l)
        if size > 100:
            str = "Too Long"
            break
        str += c * int(l)
    print(str)


if __name__ == "__main__":
    main()
