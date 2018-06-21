n = int(input())
dict = {}

for i in range(n):
    s = input().split()
    if s[0] == 'add':
        dict[s[2]] = s[1]
    if s[0] == 'get':
        if s[2] in dict.keys():
            print(dict[s[2]])
        else:
            print("None")
