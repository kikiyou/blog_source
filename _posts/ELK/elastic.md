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


elastic 存储数据的路径：

/var/lib/elasticsearch/nodes/0/indices/{nameOfYourIndex}/(0-4}/index


* 查询

全局搜索：
curl -XGET 'http://localhost:9200/_search?q=uid:10002827'


简单查询
curl -XGET 'http://localhost:9200/logstash-v5-equipment-2016.10.25/v5-equipment/_search?q=uid:10002827'


curl -XGET "http://localhost:9200/_search" -d'
{
  "query": {
    "match_all": {}
  }
}'

+ 数据备份

使用elasticdump

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