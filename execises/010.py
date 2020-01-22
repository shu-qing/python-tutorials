#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# filename：010.py
# author: shuqing

# 题目：暂停一秒输出，并格式化当前时间。

import time

while True:
    time_now = int(time.time())
    # print(time_now)
    time_local = time.localtime(time_now)
    # print(time_local)
    print(time.strftime("%Y-%m-%d %H:%M:%S", time_local))
    time.sleep(1)
