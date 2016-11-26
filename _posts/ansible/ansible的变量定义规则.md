# ansible的变量定义规则

[参考](http://stackoverflow.com/questions/30501711/accessing-nested-variable-variables-in-ansible)

从下面这个例子，可以看出ansible变量的引用规则
ansible的变量 规则 来源与jinja

变量文件 group_vars/all
内容如下：
app_env: staging

app_environments:
  staging:
    app_a:
      db_host: localhost
    app_b:
      db_host: localhost
  production:
    app_a:
      db_host: app_a-db.example.net
    app_b:
      db_host: app_b-db.example.com

Then, you should be able to use {{app_environments[app_env].app_a.db_host}} or {{app_environments[app_env]['app_a']['db_host']}} 
everywhere (Jinja templates, tasks).

### 在playbook中引用当前的变量
inventory/group_vars/g1.yml:

---
x: "value_of_x"
y: "{{x}}"
playbook:

---
- hosts: localhost
  tasks:
    - debug:
        var: hostvars['localhost']['y']