import sys

data = {}


def findAncestor(clazz, targetAncestor):
    global data
    for ancestor in data[clazz]:
        if ancestor == targetAncestor:
            return True
        elif findAncestor(ancestor, targetAncestor):
            return True
        else:
            continue
    return False


n = int(input())
while n > 0:
    line = sys.stdin.readline().rstrip()
    if ':' in line:
        clazz, ancestry = map(str, line.split(':'))
        clazz = clazz.rstrip()
        ancestors = ancestry.strip().split(' ')
    else:
        clazz = line
        ancestors = []
    if not clazz in data:
        data[clazz] = []
    data[clazz].extend(ancestors)
    n = n - 1
print(data)
q = int(input())
while q > 0:
    maybeAncestor, clazz = map(str, sys.stdin.readline().split())
    if (maybeAncestor == clazz) or findAncestor(clazz, maybeAncestor):
        print('Yes')
    else:
        print('No')
    q -= 1
