# mv

## 1. 命令格式

mv [选项] 源文件或目录 目标文件或目录

## 2. 基本功能

移动或重命名文件或目录

## 3. 常用参数

-b	若需覆盖文件，则覆盖前先行备份。

-f	force 强制的意思，如果目标文件已经存在，不会询问而直接覆盖；

-i	若目标文件 (destination) 已经存在时，就会询问是否覆盖

-n	目标文件已存在时，不会覆盖移动，而且不询问用户

-u	若目标文件已经存在，且 source 比较新，才会更新(update)

-v	显示文件或目录的移动过程

-t	--target-directory=DIRECTORY move all SOURCE arguments into DIRECTORY，即指定mv的目标目录，该选项适用于移动多个源文件到一个目录的情况，此时目标目录在前，源文件在后。

## 4. 注意事项

mv和rm一样也是一个破坏性的操作，所以在重要的目录下应当谨慎使用-f参数

## 5. 常用形式

将test文件移动到tmp目录下并改名为test1：

```console
# tree
.
├── test
└── tmp

1 directory, 1 file
# mv test tmp/test1
# tree
.
└── tmp
    └── test1

1 directory, 1 file
```

如果使用命令 `mv test tmp/` 则移动后不改名

将tmp目录移动到tmp1目录下：（mv命令在操作文件夹时不需要额外的参数）

```console
# tree
.
├── tmp
│   └── test1
└── tmp1

2 directories, 1 file
# mv tmp tmp1
# tree
.
└── tmp1
    └── tmp
        └── test1

2 directories, 1 file
```

将tmp1目录改名为tmp2：（当目标文件与源文件在同一目录下mv命令执行改名操作）

```console
# mv tmp1 tmp2
# tree
.
└── tmp2
    └── tmp
        └── test1

2 directories, 1 file
```

