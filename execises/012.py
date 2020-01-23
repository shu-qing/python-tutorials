#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# filename：012.py
# author: shuqing

# 题目：判断101-200之间有多少个素数，并输出所有素数。

num = 0
for i in range(101, 201):
    for j in range(2, i):
        if(i % j == 0):
            break
        if (j == i-1):
            print(i)
            num += 1
print(num)
