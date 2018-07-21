import sys


def read_int():
    return int(sys.stdin.readline())


# read n classes relationship queries from stdin
def read_classes(n):
    reader = (tuple(map(str.strip, line.split(':'))) for line in sys.stdin)
    classes = {}

    for i in range(n):
        key, *val = next(reader)
        if len(val) != 0:
            val = val.pop().split()
        classes[key] = val

    return classes


def read_exception_seq(q):
    reader = [line.strip() for line in sys.stdin]
    queries = list(reader)

    return queries


# print exception name that we won't catch
def check_exception_order(cl_tree, ex_seq):
    ex_order = [ex_seq.pop(0)]
    useless_ex = []

    for query in ex_seq:
        if query in ex_order or check_parent(cl_tree, query, ex_order):
            useless_ex.append(query)
        ex_order.append(query)

    return useless_ex


# check whether node_a is a child of any node in nodes_list or not
def check_parent(cl_tree, node_a, nodes_list):
    for node_b in nodes_list:
        if is_parent(cl_tree, node_a, node_b):
            return True
    else:
        return False


def is_parent(tree, child, parent, path=[]):
    path = path + [child]

    if child not in tree:
        return None
    if child == parent:
        return path

    for relation in tree[child]:
        if relation not in path:
            newpath = is_parent(tree, relation, parent, path)

            if newpath:
                return newpath
    else:
        return None


def main():
    n = read_int()
    cl_tree = read_classes(n)
    q = read_int()
    exception_seq = read_exception_seq(q)
    ans = check_exception_order(cl_tree, exception_seq)

    print(*ans, sep='\n')


if __name__ == "__main__":
    main()
