---
title: ansible 源码学习
date: 2016-09-30 10:19:44
tags: 
- ansible
- python
---

# ansible 源码学习
一直 想看ansible的源码，但一直没有时间
这次 正好利用十一 好好学习下

+ fnmatch   unix文件匹配模块
import fnmatch
import os

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.txt'):
        print file
----output
cc.txt
requirements.txt
contributors.txt


+ itertools 高效循环的迭代函数集合

+ multiprocessing