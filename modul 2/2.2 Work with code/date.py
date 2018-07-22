import datetime

a, b, c = map(int, input().split())
date = datetime.date(a, b, c)
delta = date + datetime.timedelta(int(input()))
print(delta.strftime('%Y %m %d').replace(' 0', ' '))
