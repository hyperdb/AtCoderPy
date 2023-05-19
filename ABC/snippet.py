def getString():
    return input()


def getInt():
    return int(input())


def getFloat():
    return float(input())


def getStringList():
    return input().split()


def getIntList():
    return list(map(int, input().split()))


def getFloatList():
    return list(map(float, input().split()))


def getStringRow(N):
    l = []
    for _ in range(N):
        l.append(input())
    return l


def getIntRow(N):
    l = []
    for _ in range(N):
        l.append(int(input()))
    return l


def getFloatRow(N):
    l = []
    for _ in range(N):
        l.append(float(input()))
    return l
