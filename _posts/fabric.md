# fabric学习

+ 基于字典的字符串格式化

>>> params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
>>> "%(pwd)s" % params                                    1
'secret'
>>> "%(pwd)s is not a good password for %(uid)s" % params 2
'secret is not a good password for sa'

使用字典格式化字符串更加简短，可读性也更好。

+ execfile()
 python 内置函数 可以用来执行一个文件

+ filter() / map()
    filter(function, sequence)：对sequence中的item依次执行function(item)，将执行结果为True的item组成一个List/String/Tuple（取决于sequence的类型）返回：
    >>> def f(x): return x % 2 != 0 and x % 3 != 0 
    >>> filter(f, range(2, 25)) 
    [5, 7, 11, 13, 17, 19, 23]
    >>> def f(x): return x != 'a' 
    >>> filter(f, "abcdef") 
    'bcdef'

>>>a=[1,2,3,4,5,6,7]
>>>b=filter(lambda x:x>5, a)
>>>print b
>>>[6,7]
如果filter参数值为None，就使用identity（）函数，list参数中所有为假的元素都将被删除。如下所示：
>>>a=[0,1,2,3,4,5,6,7]
b=filter(None, a)
>>>print b
>>>[1,2,3,4,5,6,7]

+ map()  和 filter() 很像只是不判断true
Format: map(function, sequence)
iterate所有的sequence的元素並將傳入的function作用於元素，最後以List作為回傳值。
請參考下面例子:

>>> a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> def fn(x):
...     return x*2
>>> c = map(fn, a)
>>> c
[2, 4, 6, 8, 10, 12, 14, 16, 18]

+ lambda()

lambda：这是Python支持一种有趣的语法，它允许你快速定义单行的最小函数，类似与C语言中的宏，这些叫做lambda的函数，是从LISP借用来的，可以用在任何需要函数的地方： 
> g = lambda x: x * 2 
> g(3) 
6 
-------------
def lambda(x)
    return x *2 
g = lambda
------------
> (lambda x: x * 2)(3) 
6

> 如果函数有多个()的话，函数 会把参数以此向前传
+ callable()
callable 函数接收一个对象，并当对象可以调用时返回 1 ，其它情况下返回 0 。可调用对象包括函数、类方法，至甚是类本身。
>> import string
>>> string.punctuation           1
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
>>> string.join                  2
<function join at 00C55A7C>
>>> callable(string.punctuation) 3
0
>>> callable(string.join)        4
1


+ reduce()

Format: reduce(function, sequence)
必須傳入一個binary function(具有兩個參數的函式)，最後僅會回傳單一值。
reduce會依序先取出兩個元素，套入function作用後的回傳值再與List中的下一個元素一同作為參數，以此類推，直到List所有元素都被取完。
請參考下面例子:

>>> a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> def fn(x, y):
...     return x+y
>>> d = reduce(fn, a)
>>> d
45

下面的圖片輔助說明上面範例程式中的reduce()是如何作用的:
![图片](https://az787680.vo.msecnd.net/user/law1009/1307/20137915243578.png)