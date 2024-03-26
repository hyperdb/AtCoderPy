# ABC-343 A - Wrong Answer
# https://atcoder.jp/contests/abc343/tasks/abc343_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()
    for i in range(10):
        if i == a + b:
            continue
        print(i)
        break


if __name__ == "__main__":
    main()
