#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# filename：break.py
# author: shuqing

for letter in "python":
    if letter == 'h':
        break
    print(letter)

i = 0
while i < 10:
    if i == 5:
        break
    i += 1
    print(i)
