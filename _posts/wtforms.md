---
title: git
date: 2016-08-14 10:19:44
tags: git
---

# wtforms 学习

+ 小理解

渲染 html时，都是把form对象传过去 
对象中的属相 就是 
<input id="all_zone" name="all_zone" type="checkbox" value="y">
这样的标签

自定义传值的话，可以使用下面的方法：
<div class="form-group  required">
<label class="control-label">{{ form.version_id.label }}</label><b>{{ form.version_id(class="form-control",value=version_id) }}</b>
</div>