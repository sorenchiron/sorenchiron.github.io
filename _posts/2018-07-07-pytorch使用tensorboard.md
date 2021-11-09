---
layout: mypost
title: pytorch使用tensorboard
categories: [小技巧,编程技术]
published: true
date: 2018-07-07
tags: [pytorch,tensorboard,deep learning]
---

Tensorboard 是一个动态可视化数值的工具，同时也能可视化静态的神经网络结构。

Tensorboard 包含两部分功能：

1. 将网络结构、动态数值以 protocol buffer 格式写到文件里。
1. 读取网络结构、读取动态数值，并展示在浏览器中。

第一部分功能，以python包形式存在。编程者 import tensorboard 从而使用API将动态的数值以protocol buffer格式，不断地写入文件。

第二部分功能，以可执行程序形式存在。这个程序在win下叫 tensorboard.exe，linux下叫 tensorboard。该程序是一个web服务器，能够不停地读取本地文件，查询是否有新数值要展示，再应答给网页。



因此，在python中，结合 pytorch 使用 tensorboard 分为两步：

* 将曲线、图片写入磁盘文件。
* 开启web服务器，读取文件并在网页展示曲线、图片。

# 第一步 写文件。 

python 包是 tensorboardX，用 pip install tensorboardX 来安装。


```python
import torch
from tensorboardX import SummaryWriter
# 设计一个小网络
class Net(torch.nn.Module):
    def __init__(self):
        super(Net,self).__init__()
        self.dense = torch.nn.Linear(in_features=10,out_features=1)
    def forward(self,x):
        return self.dense(x)

# 根据小网络实例化一个模型 net
net = Net()
# 创建文件写控制器，将之后的数值以protocol buffer格式写入到logs文件夹中，空的logs文件夹将被自动创建。
writer = SummaryWriter(log_dir='logs')
# 将网络net的结构写到logs里：
data = torch.rand(2,10)
writer.add_graph(net,input_to_model=(data,))
# 注意：pytorch模型不会记录其输入输出的大小，更不会记录每层输出的尺寸。
#      所以，tensorbaord需要一个假的数据 `data` 来探测网络各层输出大小，并指示输入尺寸。

# 写一个新的数值序列到logs内的文件里，比如sin正弦波。
for i in range(100):
    x = torch.tensor(i/10,dtype=torch.float)
    y = torch.sin(x)
    # 写入数据的标注指定为 data/sin, 写入数据是y, 当前已迭代的步数是i。
    writer.add_scalar('data/sin',y,i)

writer.close()
```

# 第二步 在命令行里使用 tensorboard 读取 protocol buffer 格式的数值：

```bash
tensorboard --logdir logs --port 80
```

这样就从logs里读取数值，并在本机80端口开启了一个web服务器


根据命令行的最后提示，访问网址，就可以看见下图了：

![](architecture.png)

![](sine_curve.png)


# 常见问题

但是你怕是看不到这两个网页了，因为一个tensorboard内部的bug，你会看到如下错误：

```TypeError: GetNext() takes 1 positional argument but 2 were given```

tensorboard根本无法启动。这点有人在[这个博客](https://blog.csdn.net/handsome_for_kill/article/details/80269595)中提到过，但是他的修复方法并不好用。

根据github开发者的issue： [1](https://github.com/tensorflow/tensorboard/issues/1146) [2](https://github.com/tensorflow/tensorboard/issues/1111)

我们发现需要做的是如下几步：

1. 若安装了tensorboardX, 先卸载： `pip uninstall tensorboardX`
1. 若安装了tb-nightly，先卸载：`pip uninstall tb-nightly`
1. 若安装了tensorboard， 先卸载：`pip uninstall tensorboard`
1. 安装tensorboard， `pip install tensorboard`注意，tensorboard要1.7以上版本，且要和tensorflow版本对应，比如tensorflow版本1.8.0，则要键入： pip install tensorboard==1.8.0， 否则tf-nightly会抱怨tensorboard 版本不对，拒绝安装。
1. 安装tb-nightly    : `pip install tb-nightly`
1. 安装tensorboardX, : `pip install tensorboardX`


好了可以用了。

<center>
Aurora 极光城
讲技术，说人话    
</center>
