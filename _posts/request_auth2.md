+ 第三个方案  tags -> v0.3.0

        if default_port and port is None and scheme is not None:
            dport = {"http": 80,
                     "https": 443,
                     }.get(scheme)
            if dport is not None:
                authority = "%s:%d" % (host, dport)
        return authority, path

        这段代码可能有bug 

``` python
    def test_AUTH_HTTPS_200_OK_GET(self):
        auth = ('requeststest', 'requeststest')
        url = 'https://convore.com/api/account/verify.json'
        r = requests.get(url, auth=auth)

def get(url, params={}, headers={}, cookies=None, auth=None):
    return request('GET', url, params=params, headers=headers, cookiejar=cookies, auth=auth)

def request(method, url, **kwargs):
    data = kwargs.pop('data', dict()) or kwargs.pop('params', dict())

    r = Request(method=method, url=url, data=data, headers=kwargs.pop('headers', {}),
                cookiejar=kwargs.pop('cookies', None), files=kwargs.pop('files', None),
                auth=kwargs.pop('auth', auth_manager.get_auth(url)))
<!-- 没有直接传入auth时 有两中情况 -->
1. auth_manager.get_auth 查询是否定义了全局 密码，有的话返回全局密码
2. 没有的话返回 None 
 
 

auth_manager = AuthManager()

class AuthManager(object):
    """Authentication Manager."""
    
    def __new__(cls):
        singleton = cls.__dict__.get('__singleton__')
        if singleton is not None:
            return singleton

        cls.__singleton__ = singleton = object.__new__(cls)

        return singleton


    def __init__(self):
        self.passwd = {}
        self._auth = {}


    def __repr__(self):
        return '<AuthManager [%s]>' % (self.method)


    def add_auth(self, uri, auth):
        """Registers AuthObject to AuthManager."""
        
        uri = self.reduce_uri(uri, False)
        self._auth[uri] = auth

    def add_password(self, realm, uri, user, passwd):
        """Adds password to AuthManager."""
        # uri could be a single URI or a sequence
        if isinstance(uri, basestring):
            uri = [uri]
            
        reduced_uri = tuple([self.reduce_uri(u, False) for u in uri])
        
        if reduced_uri not in self.passwd:
            self.passwd[reduced_uri] = {}
        self.passwd[reduced_uri] = (user, passwd)


    def find_user_password(self, realm, authuri):
        for uris, authinfo in self.passwd.iteritems():
            reduced_authuri = self.reduce_uri(authuri, False)
            for uri in uris:
                if self.is_suburi(uri, reduced_authuri):
                    return authinfo

        return (None, None)


    def get_auth(self, uri):
        uri = self.reduce_uri(uri, False)
        return self._auth.get(uri, None)


    def reduce_uri(self, uri, default_port=True):
        """Accept authority or URI and extract only the authority and path."""
        # note HTTP URLs do not have a userinfo component
        parts = urllib2.urlparse.urlsplit(uri)
        if parts[1]:
            # URI
            scheme = parts[0]
            authority = parts[1]
            path = parts[2] or '/'
        else:
            # host or host:port
            scheme = None
            authority = uri
            path = '/'
        host, port = urllib2.splitport(authority)
        if default_port and port is None and scheme is not None:
            dport = {"http": 80,
                     "https": 443,
                     }.get(scheme)
            if dport is not None:
                authority = "%s:%d" % (host, dport)
        return authority, path

    
    def is_suburi(self, base, test):
        """Check if test is below base in a URI tree

        Both args must be URIs in reduced form.
        """
        if base == test:
            return True
        if base[0] != test[0]:
            return False
        common = urllib2.posixpath.commonprefix((base[1], test[1]))
        if len(common) == len(base[1]):
            return True
        return False


    def empty(self):
        self.passwd = {}


    def remove(self, uri, realm=None):
        # uri could be a single URI or a sequence
        if isinstance(uri, basestring):
            uri = [uri]

        for default_port in True, False:
            reduced_uri = tuple([self.reduce_uri(u, default_port) for u in uri])
            del self.passwd[reduced_uri][realm]


    def __contains__(self, uri):
        # uri could be a single URI or a sequence
        if isinstance(uri, basestring):
            uri = [uri]

        uri = tuple([self.reduce_uri(u, False) for u in uri])

        if uri in self.passwd:
            return True

        return False


def _get_opener(self):
    """Creates appropriate opener object for urllib2."""

    _handlers = []

    if self.auth:
        if not isinstance(self.auth.handler, (urllib2.AbstractBasicAuthHandler, urllib2.AbstractDigestAuthHandler)):
            auth_manager.add_password(self.auth.realm, self.url, self.auth.username, self.auth.password)
            self.auth.handler = self.auth.handler(auth_manager)
            auth_manager.add_auth(self.url, self.auth)

        _handlers.append(self.auth.handler)

        _handlers.extend(get_handlers())
        opener = urllib2.build_opener(*_handlers)
        return opener.open
    else:
        return urllib2.urlopen

class Request(object):
    def __init__(self, url=None, headers=dict(), files=None, method=None,
                data=dict(), auth=None, cookiejar=None):
        if isinstance(auth, (list, tuple)):
            auth = AuthObject(*auth)
        if not auth:
            auth = auth_manager.get_auth(self.url)
        self.auth = auth
        