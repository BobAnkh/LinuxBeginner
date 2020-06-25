# cat

1. 命令格式

    cat [选项] [文件]

2. 常用参数

    -A, --show-all           等价于 -vET

    -b, --number-nonblank    对非空输出行编号

    -e                       等价于 -vE

    -E, --show-ends          在每行结束处显示 $

    -n, --number     对输出的所有行编号,由1开始对所有输出的行数编号

    -s, --squeeze-blank  有连续两行以上的空白行，就代换为一行的空白行 

    -t                       与 -vT 等价

    -T, --show-tabs          将跳格字符显示为 ^I

    -u                       (被忽略)

    -v, --show-nonprinting   使用 ^ 和 M- 引用，除了 LFD 和 TAB 之外

3. 注意事项

    tac 反向列示
