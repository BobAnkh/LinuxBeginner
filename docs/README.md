# Linux Beginner

![Help-Wanted](https://img.shields.io/badge/HelpWanted-Unfinished-red)

本项目由BobAnkh发起，旨在为Linux初学者整理一些常用命令和常用工具的文档

## To Do

- 为所有Linux命令进一步添加常用的使用情况样例以及注意事项
- 添加更多的常用工具

## How to Contribute

我们非常欢迎任何人为这个仓库添加新的内容，只要它对于这个仓库是具有意义的

### 关于提交的注意事项

你需要在fork的仓库的一个具有与你所提交的内容相关名称的单独的branch提起pull request（pr），同时，从master分支提起的pr将不会被接受。这是因为你从单独分支提起pr时，仍可以通过向该分支进行commit和push来修改内容、持续更新。对于本项目目前而言，提起的pr可以根据所属类别——Linux命令或Linux工具，分别以如下形式命名分支：`LinuxCommand/<number of command><command>`或`LinuxTool/<number of tool><tool>`。

> 例如：LinuxCommand/01ls或LinuxTool/02htop等。

此外，在pr的信息框内简单描述本次pr的主要内容，以便reviewer可以较为容易的判断和了解你的想法。同时，基于本项目的情况，可以在计划添加某一新命令或工具时，可以建立新的分支和相关文件后，以`draft pr`的形式进行序号占位，需要选择已用序号后续紧邻的序号，并且不能够使用未被merge的pr所占用的序号。如果需要进行非内容方面的更改，建议先提出issue进行讨论。

每个commit建议包含相对单独的内容（即不建议将多类修改大杂烩在一个commit中提交），同时需要在message中体现出具体更改。

> 例如，对于ls.md的修改，可以写为：

```text
Add linux command ls

- 给出了ls命令基本的命令格式
- 给出了ls命令的基本参数
- 给出了ls命令的注意事项
- 后续或可添加常用的命令参数以及具体的使用场景
```

### 关于内容的注意事项

> 目前主要以Linux命令和Linux工具为主要的工作重心，如果认为有其他方面也是可以添加的，欢迎提出issue或以类似的文件形式组织后pr

- 对于Linux命令而言，目前计划涉及内容如下：
    1. 命令格式
    2. 基本参数
    3. 注意事项（这一项可以没有），例如：在rm命令中需要注意最好不要执行形如`sudo rm -rf /`这样的命令，以避免不必要的麻烦
    4. 常用命令参数及具体的使用场景，例如：ls命令常用`ls -al`以及`ls -hal`用于查看具体各文件情况

- 对于Linux工具而言，目前计划涉及内容如下：
    1. 基本功用介绍
    2. 如何安装
    3. 如何使用（可包含基本参数和基本指令）
    4. 常见使用方式和注意事项

## 欢迎大家来为本项目贡献自己的力量，如果有问题欢迎随时提出issue或通过email等形式交流
