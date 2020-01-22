#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# filename：008.py
# author: shuqing

# 题目：输出 9*9 乘法口诀表。

for i in range(1, 10):
    for j in range(1, i+1):
        print(j, "x", i, "=", j*i, end=" ")
    print()
