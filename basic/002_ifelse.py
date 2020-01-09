#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# filename：ifelse.py
# author: shuqing

if True:
    if False:
        print("it is true.")
    else:
        print("it is false.")

    i = 0
    if (i > 0) is True:
        print(i, "is positive.")
        if (i <= 10):
            print(i, "<=10")
        else:
            print(i, ">10")
    elif (i < 0):
        print(i, "is negative.")
    else:
        print(i, "= 0")
else:
    pass
