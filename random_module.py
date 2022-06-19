import random

print(random.randint(2,9))

print(random.randrange(2,9))

l=["Arvind" , "Girindra", "Nagar", "Arjun" , "Deepak"]
print(random.choice(l))

r=random.random()
print(r)

l=[10,20,30,40,50]
random.shuffle(l)
print(l)

u=random.uniform(1,9)
print(u)