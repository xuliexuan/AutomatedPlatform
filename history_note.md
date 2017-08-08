2017.07.31(**_liexuan_**)
=========================
1. set up  base.html
    * `pip install django-compressor==1.3` and `pip install django-compressor --upgrade`, future we need study it
    * study code in <head>, you can read base.html

2017.08.01(**_liexuan_**)
-------------------------
1. 加载font-awesome的图标的时候：
    * ` <span class="fa fa-hand-lizard-o"></span> `，必须是`fa fa-xxx`这样的格式
2. HTML 相关的标签
    * `<p>` 段落
    * `<h1>` 标题,h1->h6字体越来越小
    * `<a>` 定义超链接，href
    * `<img>` 图片
         ```
         <img src="" align="" alt="" border="">
         Src: 图片路径，一般使用相对路径
         Align = left/right/top/middle/bottom,图文混排时用于和图片的对齐
         Alt: 图片无法显示时显示的文字
         Border: 边框的厚度
         ```
    * `<nav>` 导航链接
    * `<span>` 组合行内元素
    * `<li>` 定义列表项目，可用于无序列表和有序列表
    * `<ul>` 无序列表
    * `<ol>` 有序列表
    * `<class>` 定义元素的类的名称, 调用css
    * `<form>` 元素是块级元素，其前后会产生折行
    * `<hr>` 水平线标签

2017.08.06(**_liexuan_**)
-------------------------
1. django-axes，用于跟踪登录失败情况。
    * pip install django-axes
2. configuration django-axes
    * https://django-axes.readthedocs.io/en/latest/configuration.html
3. issue
    * ``` Error importing module: 'No module named 'axes.middleware''```
        * https://stackoverflow.com/questions/38786393/django-axes-installed-but-axes-middleware-module-not-available

2017.08.06(**_liexuan_**)
-------------------------
1. 升级包
    * `pip install --upgrade somepackage`
2. Add APPs
    * Add 'crispy_forms' to installed APP to achieve signup page display.

2017.08.07
-------------------------
1. issue
    * ```$ git pull
        error: You have not concluded your merge (MERGE_HEAD exists).
        hint: Please, commit your changes before merging.
        fatal: Exiting because of unfinished merge.
        ```
        * http://yijiebuyi.com/blog/5b55eb51ad49ce41e2de9c85dd4513ca.html

2017.08.08
-------------------------
1. Clean database
    * 工具: SQLiteStudio
    * 操作：打开工具，连接到对应的数据库；打开后，在对应的表单上点击右键，选择“擦除该表的数据”，即可清除数据库对应表单中的内容。
    * 注意：不能删除表单，否则会因为无法找到相应表单报错，需要重新导入数据库。

2017.08.08(**_liexuan_**)
-------------------------
1. syntax of `try and except`
    * python version 3.5 `except Exception,e:` ==> `except Exception as e:`
2.