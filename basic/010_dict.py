#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# filename：dict.py
# author: shuqing

# d = {key1 : value1, key2 : value2 }
# 不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
# 键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行

dict0 = {'name': 'shuqing', 'age': 18, 'class': 'first'}
print(dict0['name'], dict0['age'], dict0['class'])

dict0['age'] = 20
print(dict0)

dict0['gender'] = 'male'
print(dict0)

del dict0['class']
print(dict0)

print(type(dict0))
print(str(dict0))
print(dict0.get('name'))
print(dict0.__contains__('class'))
print(dict0.__len__())
print(dict0.pop('age'))
print(dict0)
dict0.clear()
print(dict0)
