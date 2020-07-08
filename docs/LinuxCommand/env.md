# env

## 1. 命令格式

env [选项] [NAME=VALUE] [COMMAND]

## 2. 基本功能

显示环境变量或在指定环境中进行操作

## 3. 常用参数

不加参数	显示当前环境所有环境变量和其值

-i	在空环境下执行命令

-u, --unset=<NAME>	在当前环境中移除指定的环境变量

-C, --chdir=<DIR>	使用指定的目录执行命令（但不会进入该目录）

## 4. 注意事项

在env命令中对环境变量的修改只在该命令行中有效，并没有实际修改/etc/profile或.bashrc文件中的值

## 5. 常用形式

显示当前环境下的所有环境变量：

```console
$ env
SHELL=/bin/bash
WSL_DISTRO_NAME=Ubuntu-20.04
LANGUAGE=C.UTF-8
...
```

