# flask源码学习

+ from __future__ import with_statement
  在老版本的python 中使用with

+  from threading import local
    为了解决各个线程中的变量传递问题，把变量存在一个全局字典中

        原来的写法是：

    v={key:value};在不同的线程里通过v[thread_name]来调用相应的变量；

    改进后的写法：

    tl=threading.local();

    tl是一个对象，对象的属性tl.v可以理解为一个字典：

    比如：在线程A中为tl.v赋值为nameA 相当于tl.v[thread_name]=nameA

    这样就实现了在不同的线程环境中有不同的值。
    ----------
    具体可以参考： [ThreadLocal](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386832845200f6513494f0c64bd882f25818a0281e80000)

+ flask first module

```
flask.py

from jinja2 import Environment, PackageLoader
from werkzeug import Request, Response, LocalStack, LocalProxy
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, InternalServerError
from werkzeug.contrib.securecookie import SecureCookie
```