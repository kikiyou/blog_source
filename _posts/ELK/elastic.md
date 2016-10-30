---
title: Elasticsearch
date: 2016-10-10 10:19:44
tags: 
- elk
---
# Elasticsearch
<!-- more -->
Elasticsearch 2.4.1
26MB 小巧好用

elasticsearch 中索引相当于database
数据清除办法
``` bash
curl -XDELETE 'http://127.0.0.1:9200/logstash-2013.03.*' 
```

* Elasticsearch 与 关系型数据库 名称对比

  |关系型数据库|elasticsearch|
  |----------|:-------------:|
  | database |  index       | 
  | table    |  type        |
  | row      | document     |
  | column   | field        |
  | row      | document     |
  | schema   | mapping      |
  | index    | （全部）       |
  | sql      | query DSL    |

* elastic 存储数据的路径：

/var/lib/elasticsearch/nodes/0/indices/{nameOfYourIndex}/(0-4}/index

* 增加

``` bash
curl -XPOST 'http://localhost:9200/index_XX/type_XX/1' -d '{
countent: "大家好"
user_name: "fox"
}'
```
* 删除

``` bash
curl -XDELETE 'http://localhost:9200/index_XX/type_XX/1' 
```

* 修改

``` bash
curl -XPUT 'http://localhost:9200/index_XX/type_XX/1' -d '{
countent: "大家好"
user_name: "foo"
}'
```
* 查询

``` bash
curl -XGET 'http://localhost:9200/index_XX/type_XX/1'
```

* 搜索

``` bash
全局搜索：
curl -XGET 'http://localhost:9200/_search?q=uid:10002827'

简单搜索
curl -XGET 'http://localhost:9200/logstash-v5-equipment-2016.10.25/v5-equipment/_search?q=uid:10002827'

* TERM - 关键词
curl -XGET "http://localhost:9200/_search" -d'{
  "query": {
    "term": {
      "user": "fox"
    }
  }
}'

* TEXT
{
  "query": {
    "text": {
      "countent": "这样那样" //会自动分割成term 这样 样那 那样
    }
  }
}

* RANGE
// 查看一个范围
{
  "query" :{
    "range" :{
      "age":{
        "from" : 10,
        "to" : 20,
        "include_lower": true,
        "include_upper":false,
        "boost" :2.0
      }
    }
  }
} 

* QUERY_STRING
{
  "query":{
    "query_string":{
      "query":" 这样 AND 那样 OR 怎样"
    }
  }
}

* WILDCARD - 通配符
{
  "query":{
    "wildcard":{"user" : "ki*y"}
  }
}

* MLT(more like this)
{
  "query":{
    "more_like_this":{
      "like_text": "这样那样",
      "min_term_freq": 1,   //关键词出现的频率
      "max_query_term": 12 
    }
  }
}

*  FACETS - 切面

  + aggregation 聚合
  + SELECT SUM(salary) GROUP BY name FROM employee;

facets  支持以下,就像sql group中支持 sum max 等
  + range
  + term status   //统计term出现的次数
  + geo distance
  + statistical //统计上的平均值 最大 最小
  + date histogram //时间分片


//查询频率最高的
{
  "query":{
    "match_all":{}
  },
  "facets":{  //分组 相当于sql 中group
    "bpmf":{  //组名
      "terms":{
        "field" : "bopomofo"
      }
    }
  }
}
// 查询频率最高的内容
{
  "query":{
    "match_all":{}
  },
  "facets":{
    "top":{
      "terms":{
        "filed": "countent","size": 100 // 前一百笔
              }
    }
  }
}

```

+ cluster
  + auto-discovery
  + auto-elected master
  + data replication / partition
    + with flexible shard /replica setting
     
+ shard  相当于 mysql 中 partition
  是介于 database 和 document之间  ，一个database 包括多个shard
  + more shard 
    + faster indexing / scaling

+ replica 相当于 mysql的 duplication
  + faster searching / failover

+ stats api

[stats api文档](http://www.elasticsearch.org/guide/reference/api/admin-cluster-nodes-stats)

+ 取得各项数据
+ 文件数、搜索次数、累计搜索时数、累计建索引时间
  + cluster/primary/node/index 各种级别
+ JVM CPU/Heap / OS /Thread /transport 使用状态

参考：
[Cool Bonsai Cool - An introduction to ElasticSearch](http://bit.ly/112xtsk)
[The Road to a Distributed Search Engine](http://bit.ly/ZqBBUt)
[elasticsearch, Big Data, Search & Analytics](http://bit.ly/11tmbyK)

+ 数据备份

使用elasticdump
``` bash
导出：
具体data配置信息
elasticdump --ignore-errors=true  --scrollTime=120m  --bulk=true --input=http://xxxxx:9200/.kibana   --output=data.json  --type=data
导出mapping信息
elasticdump --ignore-errors=true  --scrollTime=120m  --bulk=true --input=http://xxxxxx/.kibana   --output=mapping.json  --type=mapping  

导入：

导入mapping
elasticdump --input=mapping.json  --output=http://xxxxxxx:9000/.kibana --type=mapping

导入具体的kibana配置信息
elasticdump --input=data.json  --output=http://xxxxx:9000/.kibana --type=data
```