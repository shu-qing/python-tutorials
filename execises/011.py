#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# filename：011.py
# author: shuqing

# 题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
# 小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？


def total_num(month):
    if month == 1:
        return 1
    numlist = [1, 0]
    for i in range(1, month):
        numlist = [numlist[1], numlist[0]+numlist[1]]
    return numlist[0]+numlist[1]


print(total_num(10))
