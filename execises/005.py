#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# filename：005.py
# author: shuqing

# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。

list0 = []
for i in range(3):
    list0.append(int(input("input: ")))

list0.sort()
print(list0)
