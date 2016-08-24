##request 学习笔记

+  python distribution
   from distutils.core import setup
   1. 创建同模块名的目录
   2. 创建setup.py 
   3. build 打包
    $python setup sdist
   4. 安装 python setup install
        会自动把模块按照的python 默认环境中
   5.  使用时 如下
    ``` bash
   (1) 只要把你所要打包的module的py文件放到目录下，书写相应的setup.py,
   （2）执行python setup.py sdist  打包
   （3）扔到对应机器上 解包
   （4）python setup.py build  
   （5）sudo python setup.py install
    【同安装第三方模块步骤】
    ```

+ 测试
    ```
    test_requests.py
        import unittest
    ```
+ request.get
    ```
    	def __setattr__(self, name, value):
            if (name == 'method') and (value):
                if not value in self._METHODS:
                    raise InvalidMethod()
            
            object.__setattr__(self, name, value)

        ## 调用对象 可以很方便的给对象的属性赋值
        ## 特殊的属性 只接受 指定的值

+ urllib2.urlopen


+ StringIO  
    因为StringIO 的操作方式和 file的api很像，所以可以使用StringIO作为文件的  buffer 到一定量之后一次写入
    示例： https://pymotw.com/2/StringIO/
    ``` python
    # Find the best implementation available on this platform
    try:
        from cStringIO import StringIO
    except:
        from StringIO import StringIO

    # Writing to a buffer
    output = StringIO()
    output.write('This goes into the buffer. ')
    print >>output, 'And so does this.'

    # Retrieve the value written
    print output.getvalue()

    output.close() # discard buffer memory

    # Initialize a read buffer
    input = StringIO('Inital value for read buffer')

    # Read from the buffer
    print input.read()
    ```

+ 文件上传

    Python中使用POST方式上传文件 ： (http://oldj.net/article/python-upload-file-via-form-post/)

    使用 python的 poster模块
    ```
    # test_client.py
    from poster.encode import multipart_encode
    from poster.streaminghttp import register_openers
    import urllib2
    
    # 在 urllib2 上注册 http 流处理句柄
    register_openers()
    
    # 开始对文件 "DSC0001.jpg" 的 multiart/form-data 编码
    # "image1" 是参数的名字，一般通过 HTML 中的 <input> 标签的 name 参数设置
    
    # headers 包含必须的 Content-Type 和 Content-Length
    # datagen 是一个生成器对象，返回编码过后的参数
    datagen, headers = multipart_encode({"image1": open("DSC0001.jpg", "rb")})
    
    # 创建请求对象
    request = urllib2.Request("http://localhost:5000/upload_image", datagen, headers)
    # 实际执行请求并取得返回
    print urllib2.urlopen(request).read()
    ```

+ Python——eventlet 绿色线程
    [eventlet](http://www.cnblogs.com/Security-Darren/p/4170031.html)

    ```
    try:
        from eventlet.green import urllib2
    except ImportError:
        import urllib2
    ```

    ``` 引入猴子补丁
    import urllib
    import urllib2

    try:
        from gevent import monkey 
        monkey.patch_all()
    except ImportError:
        pass
        
    ```

+ 猴子补丁
    属性在运行时的动态替换，叫做猴子补丁。
    eventlet中大量使用了 猴子补丁，对标准函数进行绿化

+ gevent、eventlet twisted  非阻塞网络库
    基于协程的网络库gevent、eventl

+ request的作者认为 eventlet 性能高于 gevent
```
import urllib
import urllib2

try:
	import eventlet
	eventlet.monkey_patch()
except ImportError:
	pass

if not 'eventlet' in locals():
	try:
		from gevent import monkey 
		monkey.patch_all()
	except ImportError:
		pass
```

+ urllib2 中 urlopen() 被 opener.open() 代替

    ``` urllib2.py
    def urlopen(url, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT,
            cafile=None, capath=None, cadefault=False, context=None):
        return opener.open(url, data, timeout)
    ```


+ git管理
    三个主干
    1. release
    2. devlop
    3. feature
        feature/multiart-encode
        feature/cookiejar

+ 归纳
    1. core.py
    2. def get()
```
    r = Request()
	
	r.method = 'GET'
	r.url = url
	r.params = params
	r.headers = headers
	r.cookiejar = cookies
	r.auth = _detect_auth(url, auth)
	
	r.send()
	
	return r.response
```
    3. class Request(object):
        def __init__(self):
        def __setattr__(self, name, value):
        def _get_opener(self):
                opener = urllib2.build_opener(*_handlers)
			return opener.open
        def send():
            opener = self._get_opener()
            resp = opener(req)
            self._build_response(resp)
    新加一个方法 就要添加一个单元测试用例

+ python包导入  相对导入与绝对导入
    在python 2.x中启用 绝对导入
    from __future__ import absolute_import

[参考](http://zhuhaipeng.me/blog/2014/08/26/pythondao-ru-de-lu-jing-,jue-dui-dao-ru-,xiang-dui-dao-ru/)

+ 使用tox测试代码的兼容性
[tox](https://mozillazg.com/2014/07/python-use-tox-test-code.html)

+ 让python 记住自己的版本

    from core import __version__

[参考](http://blog.theerrorlog.com/making-python-programs-remember-their-versions.html)

+ Safer error response handling. 
    self.response.status_code = resp.code
    -----
    self.response.status_code = getattr(resp, 'code', None)

+ request.async.get() 的实现
    创建 async.py
    先引入async 再import  从core 引入get
    这时就可以 实现异步sync的get
    -->request -->async.py -->import urllib -->monkey_patch urllib -->core.py -->get()

+ 小技巧  方便传值
``` python
def get(url, params={}, headers={}, cookies=None, auth=None):
    return request('GET', url, params=params, headers=headers, cookiejar=cookies,
                    auth=_detect_auth(url, auth))

def request(method, url, **kwargs):
    r = Request(method=method, url=url, data=data, headers=kwargs.pop('headers', {}),
                cookiejar=kwargs.pop('cookies', None), files=kwargs.pop('files', None),
                auth=_detect_auth(url, kwargs.pop('auth', None)))

class Request(object):
    def __init__(self, url=None, headers=dict(), files=None, method=None,
                 data=dict(), auth=None, cookiejar=None):
        self.url = url
        self.headers = headers
        self.files = files
        self.method = method              
```