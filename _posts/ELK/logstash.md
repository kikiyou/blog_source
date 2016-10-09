---
title: logstash 学习
date: 2016-10-09 11:31:44
tags: 
- elk
---
#  logstash 学习

+ 查看当前版本
logstash --version

+ 插件安装
plugin install XXXX

+ 本机现在有多少插件可用
plugin list

原则：
Logstash 配置一定要有一个 input 和一个 output。
写明 input，默认就会使用 input/stdin ，同理，没有写明的 output 就是 output/stdout

+ collectd
    
    - 安装
    apt-get install collectd

+ 检查配置是否正确
logstash --configtest -f logstash-live-netflow.conf

+ Grok 过滤捕获
    
    - 正则捕获
    ``` bash
        grok {
            match => {
                "message" => "\s+(?<request_time>\d+(?:\.\d+)?)\s+"
            }
        }
    ```
    - Grok表达式 捕获 
    ``` bash
        grok {
        match => {
            "message" => "%{WORD} %{NUMBER:request_time:float} %{WORD}"
        }
    }
    ```

    