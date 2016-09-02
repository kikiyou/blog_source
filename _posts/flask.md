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

+ 大型项目组织
```
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()


默认 单个应用程序的写法
/yourapplication
    /yourapplication
        /__init__.py
        /static
            /style.css
        /templates
            layout.html
            index.html
            login.html
            ...

大型应用的写法
/yourapplication
    /runserver.py
    /yourapplication
        /__init__.py
        /views.py
        /static
            /style.css
        /templates
            layout.html
            index.html
            login.html
            ...

把yourapplication.py 创建同名目录，把yourapplication.py 改为同名目录下面的__init__.py
（0）runserver.py   （以后运行项目,python runserver.py）
from yourapplication import app
app.run(debug=True)

(1) __init__.py
from flask import Flask
app = Flask(__name__)

import yourapplication.views

（2） views.py 
from yourapplication import app

@app.route('/')
def index():
    return 'Hello World!'

理解：__name__ 变量会自动变为导入的包名,这样就能导入对应 应用下的模板与静态文件
```
[参考](http://docs.jinkan.org/docs/flask/patterns/packages.html)

+ python中__name__的使用 

    1. 如果模块是被导入，__name__的值为模块名字
    2. 如果模块是被直接执行，__name__的值为’__main__’

+ route函数
def route(self, rule, **options):
    def decorator(f):
        self.add_url_rule(rule, f.__name__, **options)
        self.view_functions[f.__name__] = f
        return f
    return decorator    

给一个url规则动态注册视图函数的 decorator
@app.route("/")
def hello():
    return "Hello World!"

```
如果一个url规则是 / 结尾，用户请求是会自动定向到有/结尾的页面
如果一个url规则没有/ 结尾,用户请求的是用/结尾的页面，会报404错误


+ werkzeug中的Map()

from werkzeug.routing import Map
self.url_map = Map()

werkzeug.routing中Map()的示例
    >>> m = Map([
    ...     # Static URLs
    ...     Rule('/', endpoint='static/index'),
    ...     Rule('/about', endpoint='static/about'),
    ...     Rule('/help', endpoint='static/help'),
    ...     # Knowledge Base
    ...     Subdomain('kb', [
    ...         Rule('/', endpoint='kb/index'),
    ...         Rule('/browse/', endpoint='kb/browse'),
    ...         Rule('/browse/<int:id>/', endpoint='kb/browse'),
    ...         Rule('/browse/<int:id>/<int:page>', endpoint='kb/browse')
    ...     ])
    ... ], default_subdomain='www')
    
    >>> c = m.bind('example.com')
    >>> c.build("kb/browse", dict(id=42))
    'http://kb.example.com/browse/42/'
    >>> c.build("kb/browse", dict())
    'http://kb.example.com/browse/'
    >>> c.build("kb/browse", dict(id=42, page=3))
    'http://kb.example.com/browse/42/3'
    >>> c.build("static/about")
    '/about'
    >>> c.build("static/index", force_external=True)
    'http://www.example.com/'

    >>> c = m.bind('example.com', subdomain='kb')
    >>> c.build("static/about")
    'http://www.example.com/about'

    [Flask 路由做范围限制](http://liyangliang.me/posts/2014/02/range-validation-in-flask-routing/)