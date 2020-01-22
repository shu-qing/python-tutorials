#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# filename：007.py
# author: shuqing

# 将一个列表的数据复制到另一个列表中。


List1 = [1, 2, 3, 5, 8]
List2 = List1           # 传递引用
List3 = List1[:]        # 拷贝
List1.append(13)

print(id(List1), id(List2), id(List3))  # id函数能够得到对象的地址
print(List2)
print(List3)
