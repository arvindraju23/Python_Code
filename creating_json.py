import json
d = {"course_name": "Python", "fees": 1000}
# d = dict(course_name="Python", fees=1000)
j = json.dumps(d)
print(type(j))
print(j)