# fabric学习

+ 基于字典的字符串格式化

>>> params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
>>> "%(pwd)s" % params                                    1
'secret'
>>> "%(pwd)s is not a good password for %(uid)s" % params 2
'secret is not a good password for sa'

使用字典格式化字符串更加简短，可读性也更好。
