#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# filename：013.py
# author: shuqing

# 题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

for i in range(100, 1000):
    a2 = i // 100
    a1 = (i % 100)//10
    a0 = i % 10
    if (i == a2**3 + a1**3 + a0**3):
        print(i)
