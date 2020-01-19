#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# filename：001.py
# author: shuqing

# 题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

# x + 100 = i*i
# x + 100 + 168 = j*j
# j^2 -i^2 = 168
# (j+i)(j-i) = 168
# j-i >= 1
# i < 168/2 i<=83 x<83^2-100
# i > 10

for i in range(10, 84):
    for j in range(i+1, 168-i+1):
        if (j*j-i*i == 168):
            x = i*i - 100
            print(x, i, j)
