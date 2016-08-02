#### php学习

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
    ```
    $users = fopen("users.txt","r");
    while ($line = fgets($users,4096)) {
        list($name, $occupation, $color) = explode("|", $line);
        printf("Name: %s <br />", $name);
        printf("occupation: %s <br />", $occupation);
        printf("Favorite color: %s <br />", $color);
    }
    fclose($users);
    ```
    6. print_r() 数组的友好输出

    7. 添加或删除数组
        $states = ["key" => "value","key1" => "value1"]
        （1）array_unshift($states,"key","value")
