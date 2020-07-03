# rm

## 1. 命令格式

rm [选项] 文件

## 2. 基本功能

删除文件或目录

## 3. 常用参数

-f, --force    忽略不存在的文件，从不给出提示。

-i, --interactive 进行交互式删除

-r, -R, --recursive   指示rm将参数中列出的全部目录和子目录均递归地删除。

-v, --verbose    详细显示进行的步骤

--help     显示此帮助信息并退出

--version  输出版本信息并退出

## 4. 注意事项

使用参数-f删除文件或目录是不可恢复的，因此在重要的目录下删除文件时，推荐使用-i参数，系统会提示是否进入目录或是否删除文件，此时输入'y'并回车即可确认

```console
$ mkdir -p 1/{1.1/,1.2/{1.2.1/,1.2.2}}
$ tree 1
1
├── 1.1
└── 1.2
    ├── 1.2.1
    └── 1.2.2

4 directories, 0 files
$ rm -ir 1
rm: descend into directory '1'? y
rm: remove directory '1/1.1'? y
rm: descend into directory '1/1.2'? y
rm: remove directory '1/1.2/1.2.1'? y
rm: remove directory '1/1.2/1.2.2'? y
rm: remove directory '1/1.2'? y
rm: remove directory '1'? y
```

## 5. 常用形式

使用参数-rf来删除文件也是ok的，因此在处理不重要的目录或者文件时，都可以直接使用命令：

```console
$ rm -rf <filename>
```