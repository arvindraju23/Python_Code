#Method of Function Call in Module
#Method 1
# import module1
# print(module1.sum(10, 20))
# print(module1.mul(10,20))

#Method 2
# import module1 as m
# print (m.mul(10,2))

#Method 3
from module1 import *
print(sum(10,20))
print(mul(10,30))