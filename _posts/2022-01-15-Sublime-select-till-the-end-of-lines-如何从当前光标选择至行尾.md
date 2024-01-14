---
layout: mypost
title: Sublime-select-till-the-end-of-lines-如何从当前光标选择至行尾
categories: [文章]
published: true
date: 2022-01-15
tags: [文章]
---


# 前言与应用场景

使用sublime时需要多个光标选中内容，并从当前光标一直选择至行尾。

一般而言，使用`shift+home` `shift+end` 即可选中至行首尾，但是对于使用86键，或68键小型键盘的用户，或者部分mac无线键盘用户而言，缺失 home 与 end 键会导致无法使用选中功能。

# 如何查看当前sublime的键盘快捷键
在主界面中，从顶部菜单栏依次进入 `Pereference > Key Bindings` 即可看到默认快捷键设置，左侧显示的是不可更改的默认快捷键配置，右侧是空白的用户自定义编辑区。

# 如何覆盖默认的sublime快捷键配置
在右侧空白编辑区键入的快捷键配置，将以文本形式保存在sublime程序目录下的配置文件中，快捷键优先匹配用户自行编辑的配置，用户没有自行填写配置的，即使用默认快捷键。

# 如何新增当前光标选择至行尾的快捷键
在右侧空白的用户自定义快捷键编辑区写入如下内容：

```json
[
	{ "keys": ["ctrl+alt+left"], "command": "move_to", "args": {"to": "bol", "extend": true} }, 
	{ "keys": ["ctrl+alt+right"], "command": "move_to", "args": {"to": "eol", "extend": true} },

]
```

含义如下：
```json
{ "keys": ["ctrl+alt+left"], "command": "move_to", "args": {"to": "bol", "extend": true} }
  "按键"：["ctrl+alt+右箭头"],"执行动作":"移动光标","参数"：{"移到": "begin-of-line行首","同时延伸选区":"是"}
```

# 一些常见的快捷键命令

 - scroll_lines:按行滚动
 - move:移动光标
 - new_file:新建文件
 - insert:插入
 - join_lines:多段文字拼接成一行
 - duplicate_line:复制文字
 - auto_complete:自动补全
 - insert_snippet:插入自行指定的代码模板
