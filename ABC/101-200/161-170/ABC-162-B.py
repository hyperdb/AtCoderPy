# ABC-162 B - FizzBuzz Sum
# https://atcoder.jp/contests/abc162/tasks/abc162_b
#
def getInt():
    return int(input())


def main():
    n = getInt()

    c = 0
    for i in range(1, n + 1):
        if i % 3 == 0 or i % 5 == 0:
            continue
        c += i
    print(c)


if __name__ == "__main__":
    main()
