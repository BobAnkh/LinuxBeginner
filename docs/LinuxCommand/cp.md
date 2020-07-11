# cp

## 1. 命令格式

cp [选项] 源 目录

or：cp [选项] -t 目录 源

## 2. 基本功能

复制文件或目录

## 3. 常用参数

-a, --archive 等于-dR --preserve=all

--backup[=CONTROL] 为每个已存在的目标文件创建备份

-b 类似--backup 但不接受参数

--copy-contents 在递归处理是复制特殊文件内容

-d 等于--no-dereference --preserve=links，如果源文件是软链接文件，则复制出来的文件也是软链接文件。

> -d参数对硬链接无效，复制出来的文件不是硬链接文件

-f, --force 如果目标文件无法打开则将其移除并重试(当 -n 选项存在时则不需再选此项)

-i, --interactive 覆盖前询问(使前面的 -n 选项失效)

-H 跟随源文件中的命令行符号链接

-l, --link 硬链接文件而不复制

-L, --dereference 总是跟随符号链接

-n, --no-clobber 不要覆盖已存在的文件(使前面的 -i 选项失效)

-P, --no-dereference 不跟随源文件中的符号链接

-p 等于--preserve=模式,所有权,时间戳

--preserve[=属性列表   保持指定的属性(默认：模式,所有权,时间戳)，如果可能保持附加属性：环境、链接、xattr 等

-R, -r, --recursive  复制目录及目录内的所有项目

-s 软链接文件而不复制

-u 若目标文件已经存在，且 source 比较新，才会更新(update)

## 4. 注意事项

暂无

## 5. 常用形式

将test文件不改名复制到当前目录tmp目录下:

```console
$ touch test
$ cp test tmp
$ tree
.
├── test
└── tmp
    └── test

1 directory, 2 files
```

若要改名复制，则可用命令：

```console
cp test tmp/test_p
```

复制目录：

```console
$ cp -r tmp tmp_p
$ tree
.
├── test
├── tmp
│   └── test
└── tmp_p
    └── test

2 directories, 3 files
```
