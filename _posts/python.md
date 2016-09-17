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


+ python  dict() 函数
可以很方便的 把list 转换为字典
比如：
```
list = [(key,value),(key1,value1)]
dict = dict(list)
> dict
{key:value,key1:value1}

+ 交互的输入密码
import getpass
getpass.getpass()