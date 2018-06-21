def add(scopes, cur, what):
    if cur not in scopes:
        scopes[cur] = {}
        scopes[cur]['vars'] = []
        scopes[cur]['vars'].append(what)
    else:
        if 'vars' not in scopes[cur]:
            scopes[cur]['vars'] = []
            scopes[cur]['vars'].append(what)
        else:
            scopes[cur]['vars'].append(what)


def create(scopes, cur, par):
    if cur not in scopes:
        scopes[cur] = {}
        scopes[cur]['funcs'] = []
        scopes[cur]['vars'] = []
        scopes[par]['funcs'].append(cur)
        scopes[cur]['parent'] = par
    else:
        if 'funcs' not in scopes[cur]:
            scopes[cur]['funcs'] = []
            scopes[cur]['parent'] = par
            scopes[par]['funcs'].append(cur)
        else:
            scopes[cur]['funcs'].append(cur)
            scopes[par]['funcs'].append(cur)


def search(scopes, namespace, what):
    if what in scopes[namespace]['vars']:
        return namespace
    else:
        try:
            upper_namespace = scopes[namespace]['parent']
        except KeyError:
            return None
        return search(scopes, upper_namespace, what)


n = int(input())
scopes = {'global': {'funcs': [], 'vars': []}}

for i in range(n):
    command = input().split()
    if command[0] == 'add':
        add(scopes, command[1], command[2])
    elif command[0] == 'create':
        create(scopes, command[1], command[2])
    elif command[0] == 'get':
        print(search(scopes, command[1], command[2]))
