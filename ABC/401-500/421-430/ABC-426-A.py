# ABC-426 A - OS Versions
# https://atcoder.jp/contests/abc426/tasks/abc426_a
#
def getStringMap():
    return input().split()


def main():
    os_list = ["Ocelot", "Serval", "Lynx"]
    X, Y = getStringMap()

    print("Yes" if os_list.index(X) >= os_list.index(Y) else "No")


if __name__ == "__main__":
    main()
