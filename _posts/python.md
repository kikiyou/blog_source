### python学习
python debug 工具
    pdb
    (https://docs.python.org/2/library/pdb.html)


vs code 直接输出python
http://stackoverflow.com/questions/29987840/how-to-execute-python-code-from-within-visual-studio-code

+ python 默认就有 __setattr__ 和 __getattr__方法
  可以方便的对属性赋值  而不用写set 和 get 方法

+ 动态添加属性 和 方法
  1. 属性
    obj.a = 1或setattr(obj, 'a', 1)
  2. 方法
      class A(object):
        pass
      
      a = A(object)
     (1) a.hello = types.MethodType(a, hello)
     (2) 方法二  如下
          ```
          class Student(object):
              pass
          s = Student()
          def hello():
              print "hello word!!!"

          s.hello = hello
          s.hello()
          ```
3. @property  把方法变成属性

+ python 中闭包的实现
  ```
  def addx(x):
    return lambda y: x + y

  add8 = addx(8)
  add9 = addx(9)

  print add8(100)
  print add9(100)

  闭包的作用
  
  加强模块化

```
