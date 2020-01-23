#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# filename：014.py
# author: shuqing

# 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。


def getFirstFactor(x):
    for i in range(2, x+1):
        if (x % i == 0):
            return i


def getFactorList(y, List):
    temp = getFirstFactor(y)
    List.append(temp)
    if temp == y:
        return List
    else:
        return getFactorList(int(y/temp), List)


num = int(input("input a number: "))

if num <= 0:
    print("not a valid number")

factorList = getFactorList(num, [])

index = 0
print(num, "=", end=" ")
for i in factorList:
    index += 1
    if index < len(factorList):
        print(i, "*", end=" ")
    else:
        print(i)
