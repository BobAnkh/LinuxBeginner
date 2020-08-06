# grep

## 1. 命令格式

grep [选项] 待匹配内容 [文件]

## 2. 基本功能

grep命令用来在指定文件中搜寻与待匹配内容匹配的行

## 3. 常用参数

--help  显示帮助信息并离开

-V, --version  显示版本信息并离开

-E, --extended-regexp  将输入的待匹配内容作为扩展正则表达式理解

-F, --fixed-strings  将输入的待匹配内容作为字符串而不是正则表达式理解

-G, --basic-regexp  将输入的待匹配内容作为正则表达式理解（此为默认）

-P, --perl-regexp  将输入的待匹配内容作为perl正则表达式理解

-e PATTERNS, --regexp==PATTERNS  将PATTERNS作为待匹配内容，此参数主要用于将以'-'开头的PATTERNS声明为待匹配内容

-f FILES, --file=FILES  将FILES作为读取匹配模式的源文件，每一行为一个待匹配内容，与'-e'同时使用时，对所有读取到的待匹配内容都进行搜索

-i, --ignore-case  搜索时忽略大小写区别

--no-ignore-case  搜索时不忽略大小写区别，用于取消之前的'-i'设定的忽略大小写（此为默认）

-v, --invert-match  反向搜索，结果为匹配不成功的行

-w, --word-regexp  搜索时限定匹配对象为单个的词，如hello只能与hello匹配而不能与helloworld匹配

-x, --line-regexp  搜索时限定匹配对象所在行与待匹配内容完全一致，此参数会使'-w'无效

-y  旧版本中'-i'的替代

-c, --count  输出匹配的行数而不是行内容

--color[=WHEN], --colour[=WHEN]  控制是否用色彩标明匹配成功的内容。WHEN可以是'never','always'或'auto'其中之一

-L, --files-without-match  输出未匹配的文件名而不是匹配的行内容

-l, --files-with-matches  输出匹配的文件名而不是匹配的行内容

-m NUM, --max-count=NUM  只匹配最多NUM行，匹配行数达到NUM后搜索停止

-o, --only-matching  输出匹配成功的部分（只包括待匹配内容）而不是匹配的行内容

-q, --quiet, --silent  不输出任何内容

-s, --no-messages  不输出关于不存在或无法可读的文件的错误信息

-b, --byte-offset  输出匹配成功的部分在所在文件中的位置（以byte为单位）

-H, --with-filename  输出匹配成功的部分所在的文件的名字（多文件作为搜索对象时此为默认）

-h, --no-filename   不输出匹配成功的部分所在的文件的名字（单文件作为搜索对象时此为默认）

--label=LABEL  将来标准输入当作来自名为LABEL的文件的输入处理，主要用于处理在搜索前改变了形式和内容的文件

-n, --line-number  输出匹配的部分所在行的行号

-T, --initial-tab  输出行内容之前加入一个TAB

-u, --unix-byte-offsets  输出匹配成功部分所在位置时以unix系统方式统计，必须结合'-b'使用且只在MS-Windows和MS-DOS上有实际作用

-Z, --null  在文件名后输出一个NULL字符而不是别的字符，主要用于处理文件名含有特殊字符的文件

-A NUM，--after-context=NUM  输出匹配部分所在行及其之后NUM行的内容，不同匹配结果之间以'--'隔开，不能与'-o'并用

-B NUM, --befor-context=NUM 输出匹配部分所在行及其之前NUM行的内容，不同匹配结果之间以'--'隔开，不能与'-o'并用

-C NUM, -NUM, --context=NUM 输出匹配部分所在行及其之前和之后NUM行的内容，不同匹配结果之间以'--'隔开，不能与'-o'并用

-a, --text  将二进制文件当作文本文件处理，等同于'--binary-files=text'

--binary-files=TYPE  将二进制文件当作TYPE处理，TYPE可以是'binary','text'或'without-match'其中之一

-D ACTION, --devices=ACTION  接受来自设备，FIFO和socket的文本作为搜索对象,ACTION是用于从以上来源中获取文本的指令（如read）

-d ACTION, --directories=ACTION  接受来自目录的文本作为搜索对象,ACTION是用于从目录中获取文本的指令（如read）

--exclude=GLOB  跳过对任何文件名与GLOB匹配的文件的搜索，GLOB是通配符形式

--exclude-from=FILE  跳过对任何文件名与从FILE中读取的通配符匹配的文件的搜索

--exclude-dir=GLOB  跳过对任何目录名与GLOB匹配的目录的搜索，GLOB是通配符形式

-I  不对二进制文件搜索，直接输出二进制文件不匹配，等同于'--binary-files=without-match'

--include=GLOB  只对文件名与GLOB匹配的文件进行搜索，GLOB是通配符形式

-r, --recursive  对给定的目录下所有文件（不包括软链接）进行搜索，此时需在[文件]处给出目录否则默认为当前工作目录

-R  对给定的目录下所有的文件进行搜索，此时需在[文件]处给出目录否则默认为当前工作目录

--line-buffered  输出使用行缓冲

-U, --binary  将所有文件都当作二进制文件处理而不根据文件内容猜测，只在MS-Windows和MS-DOS上有实际作用

-z, --null-data  将输入输出都当作以NULL结尾的行序列来处理，主要用于处理文件名含有特殊字符的文件

## 4. 注意事项

与find命令相比，grep主要用于对文件内容进行搜索，find命令则是对文件名进行搜索。

作为Linux最重要的文本处理工具之一的grep命令，其功能非常强大，需要对其有一定的掌握。由于grep命令主要是进行搜索匹配，所以为了更好的使用grep命令，最好能对正则表达式和通配符这两种常见的指定待匹配内容的方式有所了解，限于篇幅只在后文给出一些例子。

在使用grep时，对于二进制文件进行处理要谨慎使用'-a'参数，使用之后由于将二进制文件作为文本文件处理，很可能在输出中会产生难以预测的内容，如果此时将输出定向到命令行，这些输出有可能被系统理解为命令，会产生糟糕的结果。当然，使用'-a'可以在不知编码形式的文件中找到更多可能存在的匹配部分，尽管结果是不安全的。

## 5. 常用形式

查找file.txt文件中所有含有'object'的行

```bash
grep 'object' file.txt
```

查找file.txt文件中不含'object'的行且只打印满足条件的行数

```bash
grep -vc 'object' file.txt
```

查找当前目录中所有含有'object'的文件且列出object所在位置上下文各一行

```bash
grep -C 1 -r 'object'
```

查找file.txt文件中所有以'my'开头的行

```bash
$ cat file.txt
my friend is waiting
oh, my friend is waiting
$ grep '^my' file.txt
my friend is waiting
```

查找file.txt文件中所有以'ing'结尾的行

```bash
$ cat file.txt
my friend is waiting
my friend is waiting for me
$ grep 'ing$' file.txt
my friend is waiting
```

查找file.txt文件中首字母为g，末字母为d，长度为4的单词

```bash
$ cat file.txt
good boy
geed boy
g22d boy
god boy
golf boy
toad boy
$ grep 'g..d' file.txt
good boy
geed boy
g22d boy
```

查找file.txt文件中首字母为g，末字母为d，中间为任意个o的单词，并显示行号

```bash
$ cat file.txt
good boy
goood boy
g22d boy
god boy
golf boy
toad boy
$ grep -n 'g..d' file.txt
1:good boy
2:goood boy
4:god boy
```
