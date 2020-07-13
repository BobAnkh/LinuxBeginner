# head

## 1. 命令格式

head [参数] 文件

## 2. 基本功能

head命令可用于查看文件的开头部分的内容

## 3. 常用参数

-q 隐藏文件名

-v 显示文件名

-c<字节> 显示字节数

-n<行数> 显示的行数

## 4. 注意事项

默认head命令打印其相应文件的开头10行。可以用负数数字表示除去最后n行。

## 5. 常用形式

显示file.log文件的开头5行：

```bash
head -n 5 file.log
```

显示file.log文件的前20个字节：

```bash
head -c 20 file.log
```

显示file.log文件除最后10行外的内容：

```bash
head -n -10 file.log
```
