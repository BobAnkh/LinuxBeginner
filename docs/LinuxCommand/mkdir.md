# mkdir

## 1. 命令格式

mkdir [选项] 目录

## 2. 基本功能

新建目录

## 3. 常用参数

-m, --mode=模式，设定权限<模式> (类似 chmod)，而不是 rwxrwxrwx

e.g.: `mkdir -m 777 test3`

> 注：读写执行分别为4、2、1

-p, --parents  可以是一个路径名称。此时若路径中的某些目录尚不存在,加上此选项后,系统将自动建立好那些尚不存在的目录,即一次可以建立多个目录;

-v, --verbose  每次创建新目录都显示信息

--help   显示此帮助信息并退出

--version  输出版本信息并退出

## 4. 注意事项

若不使用参数-p创建多级目录，将会报错：

```
$ mkdir 1/2/3/4
mkdir: cannot create directory ‘1/2/3/4’: No such file or directory
```

## 5. 常用形式

一行命令创建项目的结构：

`mkdir -vp scf/{lib/,bin/,doc/{info,product},logs/{info,product},service/deploy/{info,product}}`

```console
$ tree scf/

scf/

|-- bin

|-- doc

|   |-- info

|   `-- product

|-- lib

|-- logs

|   |-- info

|   `-- product

`-- service

      `-- deploy

        |-- info

         `-- product

12 directories, 0 files
```
