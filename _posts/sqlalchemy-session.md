---
title: sqlalchemy_session
date: 2016-07-14 17:34:47
tags:
---
#sqlalchemy session管理

## session基础用法
``` python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# an Engine, which the Session will use for connection
# resources
some_engine = create_engine('mysql://root:1234@localhost/test')

# create a configured "Session" class
Session = sessionmaker(bind=some_engine)

# create a Session
session = Session()

# work with sess
result = session.execute('show variables')
for row in result:
    print row
```
### sessionmaker 应该放在哪里？
+ 如果程序启动的时候知道连接到哪个数据库，就把sessionmaker 放在 `__init__.py`中，在别的模块中 from mypackage import Session 这样引用
+ 如果程序启动的时候不知道要去连接哪个数据库，可以使用 sessionmaker.configure()


## 推荐的session 用法
``` python
from contextlib import contextmanager
class ThingOne(object):
    def go(self, session):
        session.query(FooBar).update({"x": 5})

class ThingTwo(object):
    def go(self, session):
        session.query(Widget).update({"q": 18})
@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def run_my_program():
    with session_scope() as session:
        ThingOne().go(session)
        ThingTwo().go(session)
```

##Thread-Local模式 —— 生命周期与 request 同步
``` python
Web Server          Web Framework        SQLAlchemy ORM Code
--------------      --------------       ------------------------------
startup        ->   Web framework        # Session registry is established
                    initializes          Session = scoped_session(sessionmaker())

incoming
web request    ->   web request     ->   # The registry is *optionally*
                    starts               # called upon explicitly to create
                                         # a Session local to the thread and/or request
                                         Session()

                                         # the Session registry can otherwise
                                         # be used at any time, creating the
                                         # request-local Session() if not present,
                                         # or returning the existing one
                                         Session.query(MyClass) # ...

                                         Session.add(some_object) # ...

                                         # if data was modified, commit the
                                         # transaction
                                         Session.commit()

                    web request ends  -> # the registry is instructed to
                                         # remove the Session
                                         Session.remove()

                    sends output      <-
outgoing web    <-
response
```
``` python
@app.before_request
def init_session():
    g.session = Session()

@app.tear_down_request
def close_session():
    g.session.close()
```
这其实才是最适合 web 项目的 session 管理方式。（伪代码中没有写 commit 和 rollback，可自行添加）这样即避免了连接池的过快消耗，又避免了并发问题。
这也是 SQLAlchemy 文档中推荐的做法。
绑定request 请求前申请session  request之后释放session

实践上更靠谱的一段代码可能是：
``` python
from my_web_framework import get_current_request, on_request_end
from sqlalchemy.orm import scoped_session, sessionmaker

Session = scoped_session(sessionmaker(bind=some_engine), scopefunc=get_current_request)

@on_request_end
def remove_session(req):
    Session.remove()
```
Flask-SqlAlchemy就是用上面的方法实现的












参考：
http://my.oschina.net/lionets/blog/407263

http://docs.sqlalchemy.org/en/latest/orm/session_basics.html
