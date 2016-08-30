## flask 学习

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