# ABC-425 A - Sigma Cubes
# https://atcoder.jp/contests/abc425/tasks/abc425_a
#
def getInt():
    return int(input())


def main():
    N = getInt()

    result = 0
    for i in range(1, N + 1):
        result += ((-1) ** i) * (i**3)
    print(result)


if __name__ == "__main__":
    main()
