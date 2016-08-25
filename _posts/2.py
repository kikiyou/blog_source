
使用 MethodType 动态添加方法，
还是比较麻烦的
如下方法比较简单

class Student(object):
    pass

s = Student()

def hello():
    print "hello word!!!"

s.hello = hello
s.hello()
c = s

c.hello()
