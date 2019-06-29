---
layout: mypost
title: Latex的cite包将引用标号分段问题的原因与解决方法
categories: [小技巧]
published: true
date: 2019-06-29
tags: [文章,latex,cite]
---

# 问题

latex 使用 cite 命令引用一些参考文献时，输出的结果是被逗号隔断成三段甚至更多段的，十分奇怪：

![](before.png)

而我希望输出的引用列表更加精简 如下：

    Ales Dfes Kaller Blalala[19-37] ....


# 官方文档

在 `Miktex\doc\latex\cite\cite.pdf` 中找到了cite包的pdf文档， 其中说：

> **Compression** Groups of three or more consecutive numbers are compressed
> into a range using an en-dash. For example, the (poor) list
> [7,5,6,?,4,9,8,Einstein,6] would display as [?,Einstein,4–6,6–9]. Compression
> of ranges is disabled by the [nocompress] package option.

我们发现，如果引用列表有重复的项目，就会导致无法完美缩略列表。比如上面的 6 号引用，就阻止了列表的精简合并。

# 找自己的问题

我有问题的 citation：

    \cite{
    bachmann2005exploiting,
    connah2014spectral,  重复
    connah2014spectral,  重复
    crawford2011exploring,
    du2008color,
    Jimenez2007Unsupervised,
    kotwal2010visualization,
    le2011constrained,
    liao2013hscolor,
    liao2014visualization,
    liao2016hscolor,
    liaomanifold,  重复
    liaomanifold,  重复
    mignotte2010multiresolution,
    mignotte2012bicriteria,
    najim2015fspe,
    qian2013manifold,
    Sch2014Nonlinear,
    su2014hyperspectral,
    tyo2003principal,
    V2005Multispectral
    }

修改后的 citation

    \cite{
    bachmann2005exploiting,
    connah2014spectral,
    crawford2011exploring,
    du2008color,
    Jimenez2007Unsupervised,
    kotwal2010visualization,
    le2011constrained,
    liao2013hscolor,
    liao2014visualization,
    liao2016hscolor,
    liaomanifold,
    mignotte2010multiresolution,
    mignotte2012bicriteria,
    najim2015fspe,
    qian2013manifold,
    Sch2014Nonlinear,
    su2014hyperspectral,
    tyo2003principal,
    V2005Multispectral
    }


# 成功效果：

![](after.png)