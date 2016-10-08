---
title: TODO

tags: flask中jinja模版和Vue兼容
---
# flask中jinja模版和Vue兼容

jinja 和 Vue 都是用{{ }} 

笨办法：





聪明办法：
主要思路是通过修改Jinja2的配置，让他只渲染之间的数据，注意空格，而Vue.js处理不加空格的模板。

操作：
app.jinja_env.variable_start_string = '{{ '
app.jinja_env.variable_end_string = ' }}'

就酱~这样如果使用了ide，语法高亮什么的也支持了。
jinja2: {{ site.brand }}
vue.js: {{site.brand}}

我这个项目中还使用了flask-bootstrap作为模板，不幸的是，flask-bootstrap使用的大括号都没加空格，导致页面渲染时出现问题。
所以我将flask-bootstrap源码进行了修改，安装时，只要用我的数据源安装即可git+https://github.com/Panmax/flask-bootstrap.git