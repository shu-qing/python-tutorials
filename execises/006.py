#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# filename：006.py
# author: shuqing

# 题目：斐波那契数列。


def fib(n):
    if (n == 1) or (n == 2):
        return 1
    else:
        return (fib(n-1) + fib(n-2))


N = int(input("input:"))
for i in range(1, N):
    print(fib(i))
