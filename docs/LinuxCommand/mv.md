# mv

1. 命令格式

    mv [选项] 源文件或目录 目标文件或目录

2. 常用参数

    -b ：若需覆盖文件，则覆盖前先行备份。

    -f ：force 强制的意思，如果目标文件已经存在，不会询问而直接覆盖；

    -i ：若目标文件 (destination) 已经存在时，就会询问是否覆盖！

    -u ：若目标文件已经存在，且 source 比较新，才会更新(update)

    -t  ： --target-directory=DIRECTORY move all SOURCE arguments into DIRECTORY，即指定mv的目标目录，该选项适用于移动多个源文件到一个目录的情况，此时目标目录在前，源文件在后。

3. 注意事项
