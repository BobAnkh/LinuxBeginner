# ln

## 1. 命令格式

ln [选项] <源文件> <目的文件>

## 2. 基本功能

为<源文件>创建链接

> 注：linux磁盘文件系统大多使用ext3或ext4，ext4文件系统主要将分区分为两部分：小部分用于保存文件的inode信息（文件的唯一标识符），大部分用于保存block信息（实际数据信息）。
>
> 在我们使用文件名打开文件时，实际上系统是先利用文件名得到inode，再由inode去寻找对应的block数据。
>
> 链接分为两种：软链接和硬链接。软链接类似于快捷方式，创建一个新的文件，其block信息储存了源文件的路径，在软链接下链接文件与源文件的inode不相同；硬链接则类似C语言中的指针，只是使源文件的inode对应到多个文件名上去，并不会产生新的inode和block。

## 3. 常用参数

-s	建立软链接文件（默认建立硬链接文件）

-f	在建立连接文件之后删除源文件

## 4. 注意事项

不能为目录文件创建硬链接，否则会报错：

```console
$ mkdir test
$ ln test testt
ln: test: hard link not allowed for directory
```

虽然root用户使用-d参数可以为目录文件创建硬链接，但也有可能在不同的linux版本上会失败

软链接最好使用绝对路径，否则在软链接文件移动到别的目录之后，链接会失效

## 5. 常用形式

为test.md创建硬链接文件：

```console
$ touch test.md
$ ln test.md test1.md
$ ls -i
53761720551739056 test.md  53761720551739056 test1.md
```

在其他目录下创建同名硬链接文件，此时<目标文件>直接填写目标目录即可：

```console
$ tree
.
├── son
├── test.md
└── test1.md

1 directory, 2 files
$ ln test.md son/
$ tree
.
├── son
│   └── test.md
├── test.md
└── test1.md

1 directory, 3 files
```

为目录文件创建软链接：

```console
$ ln -s son /home/jwwwb/test/son1
$ tree
.
├── son
│   └── test.md
├── son1 -> son
├── test.md
└── test1.md

2 directories, 3 files
```



