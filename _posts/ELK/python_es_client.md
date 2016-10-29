# python 的 Elasticsearch 客户端

* elasticsearch-py - The official low-level Python client for Elasticsearch.

* elasticsearch-dsl-py - The official high-level Python client for Elasticsearch.

* pyes Python connector for ElasticSearch - the pythonic way to use ElasticSearch


* query

es 查询支持两种

filter 性能优于 query

    - query

    - filter

es 的任务管理api，相当于mysql的 show processlist

GET /_tasks 
GET /_tasks?nodes=nodeId1,nodeId2 
GET /_tasks?nodes=nodeId1,nodeId2&actions=cluster:* 


* es学习内容

https://github.com/rfyiamcool/elasticsearch_parse