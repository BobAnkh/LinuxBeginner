# cat

## 1. 命令格式

    cat [选项] [文件]

## 2. 基本功能

    cat 命令用于连接文件并打印到标准输出设备上

## 3. 常用参数

    -A, --show-all           等价于 -vET

    -b, --number-nonblank    对非空输出行编号

    -e                       等价于 -vE

    -E, --show-ends          在每行结束处显示 $

    -n, --number             对输出的所有行编号,由1开始对所有输出的行数编号

    -s, --squeeze-blank      有连续两行以上的空白行，就代换为一行的空白行

    -t                       与 -vT 等价

    -T, --show-tabs          将跳格字符显示为 ^I

    -u                       (被忽略)

    -v, --show-nonprinting   使用 ^ 和 M- 引用，除了 LFD 和 TAB 之外

## 4. 注意事项

    `tac`命令用于将文件已行为单位的反序输出，即第一行最后显示，最后一行先显示，用法如下例：

    > file_1.txt内容为：第一行为line_1，第二行为line_2，第三行为空行

    ```bash
    $ cat file_1.txt
    line_1
    line_2

    $ tac file_1.txt

    line_2
    line_1
    ```

## 5. 常用形式

    使用`cat`直接显示文件内容：

    ```bash
    $ cat file_1.txt
    line_1
    line_2

    ```

    使用`cat -n`加上行号显示文件内容：
    
    ```bash
    $ cat -n file_1.txt
    1   line_1
    2   line_2
    3
    ```

    使用`cat -b`仅对非空输出行编号显示文件内容：

    ```bash
    $ cat -b file_1.txt
    1   line_1
    2   line_2

    ```

    将file_1.txt中的内容加上行号后输入file_2.txt中：

    ```bash
    cat -n file_1.txt > file_2.txt
    ```

   清空file_1.txt中的内容：

    ```bash
    cat /dev/null > file_1.txt
    ```
