class A(object):
  def __str__(self):
    c =  "this is A class"
    print c
    return c
  def __repr__(self):
    cc =  "this is repr func"
    return cc



a = A()
print a