#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# filename：continue.py
# author: shuqing

for letter in "python":
    if letter == 'h':
        continue
    print(letter)

i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)
