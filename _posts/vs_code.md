---
title: VS code的使用
date: 2016-08-18 16:10:02
tags: editor
---
#### vs code的使用
<!-- more -->
+ python 的使用安装
    1. 安装的插件
    Python
    MagicPython
    Python for VSCode
    Python-autopep8
    2. 系统中安装
    dnf install pylint


+ php的使用
    1.安装的插件
        PHP Debug
        PHP code Format
        Crane - PHP Intellisense
        phpcs
    2.系统中安装
    dnf install phpcs

+ code runner 的使用安装
1.安装插件 code runner
``` tasks.json
{
    "code-runner.executorMap": {
        "javascript": "node",
        "php": "/usr/bin/php",
        "python": "python",
        "perl": "perl",
        "ruby": "/usr/bin/ruby",
        "go": "go run"
    }
}
```
2. 使用
选中需要执行的命令
执行：Ctrl+Alt+N
停止：Ctrl+Alt+M