# 进程线程的区别(threading 源码学习)

python 中的threading 模块是对 thread模块的封装

默认thread模块是C实现的，我对C语言并不了解，幸好官方提供了dummy_thread模块，
dummy_thread 是 对thread的python 实现，通过他可以简单理解thread
注：dummy_thread 无法实现多线程

[dummy_thread](https://hg.python.org/cpython/file/2.7/Lib/dummy_thread.py)

process： single-threaded process
threaded： Multi-Threaded

+ 为什么使用线程

    1. 并行需求
    2. 避免因i/o缓慢 引起的阻塞t

+ ihooks module 的使用

``` python
import ihooks, imp, os

def import_from(filename):
    "Import module from a named file"

    loader = ihooks.BasicModuleLoader()
    path, file = os.path.split(filename)
    name, ext  = os.path.splitext(file)
    m = loader.find_module_in_dir(name, path)
    if not m:
        raise ImportError, name
    m = loader.load_module(name, m)
    return m

colorsys = import_from("/python/lib/colorsys.py")

print colorsys

<module 'colorsys' from '/python/lib/colorsys.py'>
```
ihooks 绝对路径导入

+ 线程的 启动 结束 加锁 释放

+ 把要执行的代码 放到run方法里面










参考：
[详细讲解Python线程应用程序操作](http://developer.51cto.com/art/201002/184938.htm)
[Python 多线程](http://www.runoob.com/python/python-multithreading.html)
[Python线程指南](http://www.cnblogs.com/huxi/archive/2010/06/26/1765808.html)
[python实现线程池](http://ucode.blog.51cto.com/10837891/1766332)
[Python线程池详细讲解](http://blog.csdn.net/php_fly/article/details/18155421)