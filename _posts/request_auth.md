 # request认证的支持


Add in a proper AuthManager instead of the list version that was being used.
Added support for all Auth types that python supports

+ 第一个方案  创建包含usersname password 属性的对象
``` python

def test_AUTH_HTTPS_200_OK_GET(self):
    auth = requests.AuthObject('requeststest', 'requeststest')
    url = 'https://convore.com/api/account/verify.json'
    r = requests.get(url, auth=auth)

class AuthObject(object):   ##设定用户名 密码
    def __init__(self, username, password):
        self.username = username
        self.password = password

def get(url, params={}, headers={}, cookies=None, auth=None):
    r = Request(method='GET', url=url, params=params, headers=headers,
                cookiejar=cookies, auth=_detect_auth(url, auth))


def _detect_auth(url, auth):
    """Returns registered AuthObject for given url if available, defaulting to
    given AuthObject.
    """
    return _get_autoauth(url) if not auth else auth


def _get_autoauth(url):
    """Returns registered AuthObject for given url if available."""

    for (autoauth_url, auth) in AUTOAUTHS:
        if autoauth_url in url:
            return auth
    return None

AUTOAUTHS = []   ##配合全局认证的  全局参数

class Request(object):
    def __init__(self, url=None, headers=dict(), files=None, method=None,
                params=dict(), data=dict(), auth=None, cookiejar=None):

    
def _get_opener(self):
    if self.auth or self.cookiejar:
        if self.auth:
            authr = urllib2.HTTPPasswordMgrWithDefaultRealm()
            authr.add_password(None, self.url, self.auth.username, self.auth.password)


def add_autoauth(url, authobject):   ##自动认证  比如输入一次  以后访问自动传参数
    """Registers given AuthObject to given URL domain. for auto-activation.
    Once a URL is registered with an AuthObject, the configured HTTP
    Authentication will be used for all requests with URLS containing the given
    URL string.

    Example: ::
        >>> c_auth = requests.AuthObject('kennethreitz', 'xxxxxxx')
        >>> requests.add_autoauth('https://convore.com/api/', c_auth)
        >>> r = requests.get('https://convore.com/api/account/verify.json')
        # Automatically HTTP Authenticated! Wh00t!

    :param url: Base URL for given AuthObject to auto-activate for.
    :param authobject: AuthObject to auto-activate.
    """

    global AUTOAUTHS

    AUTOAUTHS.append((url, authobject))

```

+ 第二个方案 简化直接使用 list 传入
``` python
    >>> conv_auth = ('requeststest', 'requeststest') ##username password
    >>> r = requests.get('https://convore.com/api/account/verify.json', auth=conv_auth)

---------- 
auth = ('username','password')
auth[0]
auth[1]
def _get_opener(self):
    if self.auth or self.cookiejar:
        if self.auth:
            authr = urllib2.HTTPPasswordMgrWithDefaultRealm()

            authr.add_password(None, self.url, self.auth[0], self.auth[1])
            auth_handler = urllib2.HTTPBasicAuthHandler(authr)

            _handlers.append(auth_handler)
------------
```

+ 第三个方案 

    def test_AUTH_HTTPS_200_OK_GET(self):
        auth = ('requeststest', 'requeststest')
        url = 'https://convore.com/api/account/verify.json'
        r = requests.get(url, auth=auth)

class Request(object):
    def __init__(self, url=None, headers=dict(), files=None, method=None,
                data=dict(), auth=None, cookiejar=None):
        if isinstance(auth, (list, tuple)):
            auth = AuthObject(*auth)
        if not auth:
            auth = auth_manager.get_auth(self.url)
        self.auth = auth