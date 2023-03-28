# ABC-184 B - Quizzes
# https://atcoder.jp/contests/abc184/tasks/abc184_b
#
def getIntMap():
    return map(int, input().split())


def getString():
    return input()


def main():
    n, x = getIntMap()
    s = list(getString())

    for a in s:
        x += 1 if a == 'o' else -1
        x = max(x, 0)
    print(x)


if __name__ == "__main__":
    main()
