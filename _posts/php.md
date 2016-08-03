#### php学习
+ 字符串输出
    1. echo | print
        >echo "string"

        >print "string"

    2. printf
        >printf("my love is %s", 'ljq')

    3. sprinf
        >$str = printf("my love is %s", 'ljq')

        >把字符串赋值给变量，而不是打印输出
+ 类型相关
    1. 获取类型
        string gettype(mixed var)
    2. 转换类型
        boolean settype(mixed var, string type)

+ echo 和 print的区别

    echo 可以输出多个参数

    void echo(string argument1[,....string argumentN])
+ var_dump()
   void var_dump ( mixed $expression [, mixed $... ] )

   显示变量信息，方便debug使用
+ php中显示错误信息 修改php.ini 如下

    1. display_errors = On

    2. error_reporting = E_ALL &~E_NOTICE

    在apache中

    1.php_flag display_errors On

    2.php_alue error_reporting 2039

+ 控制语句
    1. if语句
    ``` php

    if (condition) {
        # code...
    }

    if (condition) echo "";

    if (condition) {
        # code...
    } else {
        # code...
    }

    $retVal = (condition) ? a : b ;
    ```
    2.switch 语句
    ```
    switch (variable) {
        case 'value':
            # code...
            break;

        default:
            # code...
            break;
    }
    ```
    3.循环语句
    ``` php
    while ($a <= 10) {
        # code...
    }

    do {
        # code...
    } while ($a <= 10);

    for ($i=0; $i < ; $i++) {
        # code...
    }
    ```
    4.foreach语句

    ``` php

    $links = array("a.cn","b.cn","c.cn")
    foreach ($links as $link) {
        echo $link,'</br>';
    }

    $links = array('百度' => 'baidu.com' ,'谷歌' => 'google.com',
    '搜狗' => 'sougou.com');

    foreach ($links as $title => $link) {
        echo $title, $link;
    }
    ```
    4.文件包含语句
    ``` php
    include "lib/php/init.inc.php"
    require_once "lib/php/init.inc.php"

    条件include / require
    if (condition) {
        include "lib/php/true.php"
    } else {
        include "lib/php/fail.php"
    }

    只包含一次 include_once /  require_once
    include_once()
    require_once()
    ```

+ 函数 function
    ``` php
    1. 基本函数
    function FunctionName($value='')
    {
        # code...
    }

    2.按引用传递参数
    $cost = 20.99;
    $tax = 0.0575;
    function calculateCost(&$cost, $tax)
    {
        $cost = $cost + ($cost * $tax);
        $tax += 4;
    }
    calculateCost($cost,$tax);
    printf("Tax is %01.2f%%<br />",$tax*100);
    printf("Cost is $%01.2f",$cost);

    3.返回多个值
    function retrieveUserProfile()
    {
        $user[] = "Jason";
        $user[] = "jason@example.com";
        $user[] = "English";
        return $user;
     }

     list($name,$email,$language) = retrieveUserProfile();
     echo "Name:$name, email:$email, language:$language";
     ```
+ 数组
    php中的数组实际上包含了python的字典
    ``` php
    - 创建数组
    1. $state[0] = "Delaware";

    2. 自动创建
       $state[] = "huawin";
       $state[] = "yip";
       $state[] = "tom";

    3. 创建关联数组
        $state['devops'] = 'tom'
        $state['dev'] = 'yip'

    4.使用arrary创建
        （1）索引数组
            $languages = arrary("english","Gaelic","Spanish");
        （2）关联数组
            $languages = array("Spain" => "Spanish","Treland" => "Gaelic");
         (3) php 5.4 起
        $array = ["foo" => "bar","bar" => "foo",];

    5. 使用list() 提取数组
    $users = fopen("users.txt","r");
    while ($line = fgets($users,4096)) {
        list($name, $occupation, $color) = explode("|", $line);
        printf("Name: %s <br />", $name);
        printf("occupation: %s <br />", $occupation);
        printf("Favorite color: %s <br />", $color);
    }
    fclose($users);

    6. print_r() 数组的友好输出

    7. 添加或删除数组
        $states = ["key" => "value","key1" => "value1"]

        (1) 在数组头添加元素
        array_unshift($states,"key","value");

        (2) 在数组尾添加元素
        array_push($states,"key","value");

        (3) 在数组头删除元素
        arrary_shift($states);

        (4) 从数组尾删除元素
        array_pop($states);

    8. 定位数组元素
    $states = ["key" => "value","key1" => "value1"]
        (1) 判断元素是否存在  true|false
            in_array("key",$states)

        (2) 搜索关联数组
            array_key_exists("key",$states)

        (3) 搜索关联数组的值
            array_search("vale",$states)

        (4) 获取数组中所有key
        $keys = array_keys($states);
        print_r($keys)
        OutPut----
        Array([0] => key1 [1] ==> key2)

        (5) 获取数组中的所有value
            values = array_values($states);
            print_r($values)
        OutPut----
        Array([0] => value, [1] => value1)

        (6) 获取当前数组key
        //key()
        while($key = key($states)){
            printf("$s </br",$key);
            next($states)
        }
        OutPut----
        key
        key1

        (7) 获取当前数组的值
        //current()
        while($value = current($states)){
            printf("$s </br",$value);
            next($states)
        }
        OutPut----
        value
        value1

        (8) 获取当前数组的键和值
        //each
        返回当前的键值对，并使指针推进一个位置。
        $current_states =  each($states);
        print_r($current_states)
        OutPut----
         Array([0] => key, [1] => value)

        (9) 移动数组指针到下一个位置
        //next($states)
        $names = ["tom", "yip", "ljq"];
        $name = next($names); //returns "yip"

        (10) 移动指针到前一个位置
        //prev($states)

        (11) 将指针移到第一个位置
        //rest($states)

        (12) 将指针移动到最后一个数组位置
        //end($states)

        (13) 向函数传递数组值
        //arry_walk()

        (14) 确定数组的大小和唯一性
           1. count() /sizeof() 统计大小
           2. array_count_values() 统计出现频率

        (15) 确定唯一的数组元素
        array_unique()

        (16) 数组排序
        1. array_reverse($states)  逆序
        2. sort() 由底到高
        3. natsort 自然排序

        （17）置换数组key和value的值
        array_flip($states)

        （18）合并数组
            new_states = array_merge_recursive($states1, $states2);

+ 面向对象
    1. 构造函数
    function __construct([arg,agr1,agr2.....])

    调用父类的构造函数 
    //parent
    parent::__construct();

    2. 析构函数
    function __destruct()

    3. 静态类型
    self::$visitors++; //赋值

    Visitor::getVisitors(); //引用
    静态字段和方法需要使用self关键字和类名应用

    4. instanceof关键字
    $manager = new Employee();
    .....
    if ($manager instanceof Emplyee) echo "Yes";
    //判断manager的对象是否为类Employee的实例

    5. 辅助函数
    （1） boolean class_exists(string class_name)
        确定类是否存在

    （2） string get_class(object object)
        确定对象上下文

    （3） array get_class_methods( class_name)
        了解类方法：函数返回一个数组，其中包含class_name类中低昂以的所有方法名

    （4）array get_declared_classes(void) 
        了解类字段:返回关联数组，包含object可用的字段和其值

    （5）string get_parent_class(object)
        确定对象的父类

    （6）boolean interface_exists(string interface_name)
        确定一个接口是否存在
    
    （7）boolean is_a(object object,string class_name)
        确定对象类型
    （8）boolean is_subclass_of(object object, string class_name)
        确定对象的子类类型
    （9）boolean method_exists(object object,string method_name)
        确定方法是否存在

    6.自动加载对象
    old-->
    require_once("class/Books.class.php")
    require_once("class/Employees.class.php")

    new-->
    function __autoload($class){
        require_once("class/$class.class.php")
    }

    自动加载通过定义特殊的__autoload函数，当引用未在脚本中定义的类时，自动调用这个函数。

+ 高级oop特性
    1. 对象克隆
    destinationObject = clone targetObject;
    
    1.1 __clone() 方法
        function __clone(){
            $this->tiecolor = "blue";
        }
        //在执行clone时会自动调用__clone()方法

    2. 继承
    class child_class extends parent_class{
        function new_metchod(){
            print "new_metchod"
        }
    }

    2.1 继承时构造函数的处理
        （1）子类没有构造函数，父类有  会执行父类的
        （2）子类有构造函数  不论父类有没有 都会执行子类的
        （3）如果想执行父类的构造函数 子类的构造函数如下写
            function __construct($name){
                parent::__construct($name);
                echo "<p> child class construct function</p>"
            }
        （4）如果向多个父类的构造函数都要执行，可以使用显式的 引用

    3. 接口 （接口是为了不支持多重继承而设置的，python支持多重继承，所以没有接口）
        接口：声明了所需的函数和常量，但不指定如何实现。
        interface interface_name{
            function method_name1();
        }
        class Class_Name implements interface_name{
            function method_name1()
            {
                //接口方法的实现
            }
        }

    3.1 实现多个接口
        interface IEmployee {...}
        interface IDeveloper {...}
        interface IPillage {...}

        class Employee implements IEmployee， IDeveloper， iPillage{
            ...
        }

        class Contractor implements IEmployee， IDeveloper{
            ...
        }
    
    4. 抽象类
        抽象类：不能实例化的类，只能作为i由其他类继承的基类。

        abstract class Class_Name
        {
            // insert attribute definition here
            // insert method definition here
        }
    5. 命名空间介绍 （python 不支持 namespace这种写法）