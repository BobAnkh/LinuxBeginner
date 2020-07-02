# tar

## 1. 命令格式

tar [必要参数] [选择参数] [文件]

## 2. 基本功能

## 3. 常用参数

> 必要参数有如下：

```text
-A 新增压缩文件到已存在的压缩

-B 设置区块大小

-c 建立新的压缩文件

-d 记录文件的差别

-r 添加文件到已经压缩的文件

-u 添加改变了和现有的文件到已经存在的压缩文件

-x 从压缩的文件中提取文件

-t 显示压缩文件的内容

-z 支持gzip解压文件

-j 支持bzip2解压文件

-Z 支持compress解压文件

-v 显示操作过程

-l 文件系统边界设置

-k 保留原有文件不覆盖

-m 保留文件不被覆盖

-W 确认压缩文件的正确性
```

> 可选参数如下：

```text
-b 设置区块数目

-C 切换到指定目录

-f 指定压缩文件

--help 显示帮助信息

--version 显示版本信息
```

## 4. 注意事项

## 5. 常用形式

`打包非压缩形式.tar：`

解包：tar -xvf FileName.tar

打包：tar -cvf FileName.tar FileName

`打包压缩形式.tar.gz：`

解压：tar -zxvf FileName.tar.gz

压缩：tar -zcvf FileName.tar.gz FileName

`打包压缩形式.tar.bz2：`

解压：tar -jxvf FileName.tar.bz2

压缩：tar -jcvf FileName.tar.bz2 FileName
