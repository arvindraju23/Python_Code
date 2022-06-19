import json

d = '{"cname": "Python", "fees": 1000, "duration": "4months"}'

x = json.loads(d)
print(type(x))
print(x)
for a in x:
    print(a, x[a])
