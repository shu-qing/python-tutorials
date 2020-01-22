#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# filename：tuple.py
# author: shuqing

# Python的元组与列表类似，不同之处在于元组的元素不能修改。
# 元组使用小括号，列表使用方括号。

tup1 = ('physics', 'chemistry', 1997, 3232)
tup2 = (1, 1, 2, 3, 5, 8, 11)
tup3 = ()
tup4 = (8, )

print(tup1)
print(tup2)
print(tup1+tup2)
print(tup4[0])
print(tup4*4)
