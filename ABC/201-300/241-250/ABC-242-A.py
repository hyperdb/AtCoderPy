# ABC-242 A - T-shirt
# https://atcoder.jp/contests/abc242/tasks/abc242_a
#
def getIntMap():
    return map(int, input().split())

def main():
    a, b, c, x = getIntMap()

    print(1.0 if x <= a else 0.0 if x > b else (c / (b - a)))

if __name__ == "__main__":
    main()