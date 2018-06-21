objects = [1, 2, 3, 4, 3, 2]
sets = []
for i in objects:
    if i not in sets:
        sets.append(i)
print(len(sets))
