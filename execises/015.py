#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# filename：015.py
# author: shuqing

# 题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

score = int(input("please input score: "))

if score >= 90:
    print("A")
elif (score >= 60) and (score <= 89):
    print("B")
else:
    print("C")
