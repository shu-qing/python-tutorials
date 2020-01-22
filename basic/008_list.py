#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# filename：string.py
# author: shuqing

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]

print(list1, list1[0])
print(list2, list2[1:3])
print(list3, list3[2:3])

list1.append(5)
list2.append("hello")
list3.append('x')

print(list1)
print(list2)
print(list3)

del list1[0]
del list2[2]
del list3[1:3]

print(list1)
print(list2)
print(list3)
print(len(list1), len(list2), len(list3))
print(list1+list2)
print(list3*3)

for x in list3:
    print(x)
