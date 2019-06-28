---
layout: mypost
title: MACOSX苹果电脑如何读写NTFS文件系统的U盘或移动硬盘
categories: [小技巧]
published: true
date: 2019-06-19
tags: [mac,ntfs]
---


# 插入U盘，查看盘符

插入U盘，桌面出现磁盘图标，记住磁盘图标下方的标记名称，也就是U盘的名字, 例如我的盘就叫```MyDisk```

# 找到设备号

打开一个Terminal，输入 ```mount``` 回车

可能会看到：

```bash
sysfs on /sys type sysfs (rw,nosuid,nodev,noexec,relatime,seclabel)
proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)
devtmpfs on /dev type devtmpfs (rw,nosuid,seclabel,size=7856496k,nr_inodes=1964124,mode=755)
securityfs on /sys/kernel/security type securityfs (rw,nosuid,nodev,noexec,relatime)
devpts on /dev/pts type devpts (rw,nosuid,noexec,relatime,seclabel,gid=5,mode=620,ptmxmode=000)
pstore on /sys/fs/pstore type pstore (rw,nosuid,nodev,noexec,relatime)
efivarfs on /sys/firmware/efi/efivars type efivarfs (rw,nosuid,nodev,noexec,relatime)
configfs on /sys/kernel/config type configfs (rw,relatime)
/dev/mapper/centos-root on / type ext4 (rw,relatime,seclabel,data=ordered)
selinuxfs on /sys/fs/selinux type selinuxfs (rw,relatime)
systemd-1 on /proc/sys/fs/binfmt_misc type autofs (rw,relatime,fd=32,pgrp=1,timeout=0,minproto=5,maxproto=5,direct,pipe_ino=37101)
mqueue on /dev/mqueue type mqueue (rw,relatime,seclabel)
hugetlbfs on /dev/hugepages type hugetlbfs (rw,relatime,seclabel)
debugfs on /sys/kernel/debug type debugfs (rw,relatime)
/dev/mapper/centos-home on /home type ext4 (rw,relatime,seclabel,data=ordered)
/dev/fuse on /run/user/1002/doc type fuse (rw,nosuid,nodev,relatime,user_id=1002,group_id=1002)
/dev/sda2 on /boot type ext4 (rw,relatime,seclabel,data=ordered)
/dev/sda1 on /boot/efi type vfat (rw,relatime,fmask=0077,dmask=0077,codepage=437,iocharset=ascii,shortname=winnt,errors=remount-ro)
/dev/disk1s1 on /Volumes/MyDisk .................
```
注意最后这行
```bash
/dev/disk1s1 on /Volumes/MyDisk
```

这说明设备号是 ```/dev/disk1s1```

# 卸载设备

```bash
sudo umount /Volumes/MyDisk
```

# 创建一个空文件夹

```bash
mkdir ~/Desktop/MyDisk
```

# 重新挂载NTFS格式的U盘

```bash
sudo mount -t ntfs -o rw,nobrowse /dev/disk1s1 ~/Desktop/MyDisk
```

各个参数的意思：

    -t ntfs             NTFS 格式
    -o rw,nobrowse      read write 不在桌面额外展示一个Disk图标，不自动打开
    /dev/disk1s1        要被挂载的设备号
    ~/Desktop/MyDisk    挂载到什么路径


# 使用完成后

正常弹出、或卸载U盘

然后拔出U盘

# 如果你乐意

那就删除桌面的空文件夹MyDisk

# 这一切是为了什么？

现实情况是这样：
NTFS 表示 New Technology File System，是微软随 Windows NT 开发的文件系统。 微软给这玩意申请了专利。 该文件系统的详细定义属于商业秘密 ，微软已经将其注册为知识产权产品。

我猜测，具有专利可能意味着**NTFS的写入算法**不许其他商业公司无授权的情况下商用，不许卖钱。鉴于linux是完全免费的开源操作系统，其配备了ntfs读写功能在法律上应该不存在“商业使用”的顾虑的，这些顾虑都交给使用Linux的商加自行承担了。
但是Mac有明确的开发收益公司Apple，售卖Mac也是商业行为，用了的话可能直接就抓到了。这就导致Apple不敢明着支持NTFS完整功能。

另外我也猜测，Apple基于Unix血脉，阵营上属于ext、xfs、btrfs、jfs用vfs套起来的套路，Apple可能更容易基于这类日志型文件系统做统一的读写优化。 相比之下，NTFS中文翻译为新科技文件系统，于1993年发布，时至今日已经过去了数十年，所以可能因此也不鼓励NTFS的使用。

最后我猜测，苹果在文件系统等等标准上难免是有私心的，至少为了性能和塑造技术壁垒考虑也有理由强推自己发明的文件格式，苹果推出HFS也是一个信号，这或许意味着NTFS成为了苹果的一枚小绊脚石，要像flash、光驱、耳机接口、USB接口一样被淘汰了