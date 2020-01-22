#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# filename：004.py
# author: shuqing

# 题目：输入某年某月某日，判断这一天是这一年的第几天？


def isLeapYear(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                isLeapYear = 1
            else:
                isLeapYear = 0
        else:
            isLeapYear = 1
    else:
        isLeapYear = 0
    return isLeapYear


year = int(input("year: "))
month = int(input("month: "))
day = int(input("day: "))
whichday = 0

mdays = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
for i in range(0, month-1):
    whichday += mdays[i]
    i += 1

if month > 2:
    whichday += isLeapYear(year)

whichday += day
print(whichday)
