# touch

## 1. 命令格式

touch [选项] 文件

## 2. 基本功能

可更改文档或目录的日期时间，包括访问时间和数据修改时间，也常用于创建新文件

## 3. 常用参数

> 注：Linux系统中，每个文件拥有3个时间参数（可通过stat命令进行查看）：访问时间（Access time / atime），数据修改时间（Modify time / mtime），状态修改时间（Change time / ctime）

-a   或--time=atime或--time=access或--time=use 　只更改访问时间。

-c   或--no-create 　不建立任何文档。

-d   使用指定的日期时间，而非现在的时间。

> 注：-d  <string> 使用指定的字符串 <string> 作为指定文件相应时间戳记的新值．由于<string>的规则非常灵活，在这里仅列出几个例子：
>
> `"Sun, 29 Feb 2004 16:21:42 -0800"`
>
> `"2004-02-29 16:21:42"`
>
> `"next Thursday"`

-f 　此参数将忽略不予处理，仅负责解决BSD版本touch指令的兼容性问题。

-m   或--time=mtime或--time=modify 　只更改数据修改时间。

-r 　把指定文档或目录的atime和mtime设成和参考文档或目录相同。

-t 　使用指定的日期时间，而非现在的时间。

> 注：-t  time 使用指定的时间值 time 作为指定文件相应时间戳记的新值．此处的 time规定为如下形式的十进制数:
>
> [[CC]YY]MMDDhhmm[.SS]
>
> 这里，CC为年数中的前两位，即”世纪数”；YY为年数的后两位，即某世纪中的年数．如果不给出CC的值，则touch将把年数CCYY限定在1969--2068之内．MM为月数，DD为天数，hh 为小时数(几点)，mm为分钟数，SS为秒数．此处秒的设定范围是0--61，这样可以处理闰秒．这些数字组成的时间是环境变量TZ指定的时区中的一个时间．由于系统的限制，早于1970年1月1日的时间是错误的。

## 4. 注意事项

touch指令只能对文件的atime和mtime进行随心所欲的修改，而ctime则自动更新为使用touch命令的当前时间。

## 5. 常用形式

可以直接使用`touch 文件`来创建尚未存在的文件

```console
$ ls

$ touch file_1.txt
$ ls
file_1.txt
```

更新file1.txt的时间戳与file2.txt相同

```console
$ ls -al
total 12
drwxr-xr-x  2 root root 4096 Jul  1 09:48 ./
drwx------ 13 root root 4096 Jul  3 23:09 ../
-rw-r--r--  1 root root    0 Jul  1 09:48 file1.txt
-rw-r--r--  1 root root    6 Jul  3 23:11 file2.txt
$ touch -r file2.txt file1.txt
$ ls -al
total 12
drwxr-xr-x  2 root root 4096 Jul  1 09:48 ./
drwx------ 13 root root 4096 Jul  3 23:09 ../
-rw-r--r--  1 root root    0 Jul  3 23:11 file1.txt
-rw-r--r--  1 root root    6 Jul  3 23:11 file2.txt
```

设定file1.txt的时间戳，以`-t`参数指定的时间值

```console
$ ls -al
total 12
drwxr-xr-x  2 root root 4096 Jul  1 09:48 ./
drwx------ 13 root root 4096 Jul  3 23:09 ../
-rw-r--r--  1 root root    0 Jul  3 23:11 file1.txt
-rw-r--r--  1 root root    6 Jul  3 23:11 file2.txt
$ touch -t 201801011122.33 file1.txt
total 12
drwxr-xr-x  2 root root 4096 Jul  1 09:48 ./
drwx------ 13 root root 4096 Jul  3 23:09 ../
-rw-r--r--  1 root root    0 Jan  1  2018 file1.txt
-rw-r--r--  1 root root    6 Jul  3 23:11 file2.txt
```
