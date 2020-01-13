#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# filename：001.py
# author: shuqing

# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

num = 0
for x1 in range(1, 5):
    for x2 in range(1, 5):
        for x3 in range(1, 5):
            if (x1 != x2) and (x1 != x3) and (x2 != x3):
                num += 1
                print(x1, x2, x3)
print("totoal:", num)
