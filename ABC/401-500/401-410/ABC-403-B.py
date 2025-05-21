# ABC-403 B - Four Hidden
# https://atcoder.jp/contests/abc403/tasks/abc403_b
#
def getString():
    return input()


def main():
    T = getString()
    U = getString()

    al = len(T)
    pl = len(U)

    r = False
    for i in range(0, al - pl + 1):
        x = T[i : i + pl]
        y = [0 if x[i] == U[i] or x[i] == "?" else 1 for i in range(pl)]

        if sum(y) == 0:
            r = True
            break

    print("Yes" if r else "No")


if __name__ == "__main__":
    main()
