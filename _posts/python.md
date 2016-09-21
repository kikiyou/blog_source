### python学习
python debug 工具
    pdb
    (https://docs.python.org/2/library/pdb.html)


vs code 直接输出python
http://stackoverflow.com/questions/29987840/how-to-execute-python-code-from-within-visual-studio-code

+ python 默认就有 __setattr__ 和 __getattr__方法
  可以方便的对属性赋值  而不用写set 和 get 方法

+ 动态添加属性 和 方法
  1. 属性
    obj.a = 1或setattr(obj, 'a', 1)
  2. 方法
      class A(object):
        pass
      
      a = A(object)
     (1) a.hello = types.MethodType(a, hello)
     (2) 方法二  如下
          ```
          class Student(object):
              pass
          s = Student()
          def hello():
              print "hello word!!!"

          s.hello = hello
          s.hello()
          ```
3. @property  把方法变成属性

+ python 中闭包的实现
  ```
  def addx(x):
    return lambda y: x + y

  add8 = addx(8)
  add9 = addx(9)

  print add8(100)
  print add9(100)

  闭包的作用

  加强模块化

```
+ locals() 和 globals()
  局部命名空间 和 全局命名空间

  python中namespace只是一个字典，它的键字就是变量名，字典的值就是那些变量的值。
 
 locals 是只读的，globals 不是

例 4.10. locals 介绍

>>> def foo(arg):  
...     x = 1
...     print locals()
...     
>>> foo(7)        
{'arg': 7, 'x': 1}
>>> foo('bar')    
{'arg': 'bar', 'x': 1}
------
globals 介绍
#!/bin/bash

if __name__ == "__main__":
    for k, v in globals().items(): 
        print k, "=", v
-----        
✗ python 1.py
__builtins__ = <module '__builtin__' (built-in)>
__name__ = __main__
__file__ = 1.py
__doc__ = None
__package__ = None

参考 [locals 和 globals](http://www.chinesepython.org/pythonfoundry/limodoupydoc/dive/html/dialect_locals.html)

+ functools 模块
functools 模块中有三个主要的函数 partial(), update_wrapper() 和 wraps()。
[参考](http://blog.jkey.lu/2013/03/15/python-decorator-and-functools-module/)

``` python
wraps(wrapped[, assigned][, updated])
wraps() 函数把用 partial() 把 update_wrapper() 给封装了一下。
貌似是方便加注释的

def wraps(wrapped,
          assigned = WRAPPER_ASSIGNMENTS,
          updated = WRAPPER_UPDATES):

    return partial(update_wrapper, wrapped=wrapped,
                   assigned=assigned, updated=updated)

好，接下来看一下是如何使用的，这才恍然大悟，一直在很多开源项目的代码中看到如下使用。

from functools import wraps
def my_decorator(f):
     @wraps(f)
     def wrapper(*args, **kwds):
         print 'Calling decorated function'
         return f(*args, **kwds)
     return wrapper

@my_decorator
def example():
    """这里是文档注释"""
    print 'Called example function'

example()

# 下面是输出
"""
Calling decorated function
Called example function
"""
print example.__name__ # 'example'
print example.__doc__ # '这里是文档注释'
````