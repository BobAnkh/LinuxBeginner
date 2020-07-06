# Linux Beginner

![Help-Wanted](https://img.shields.io/badge/HelpWanted-Unfinished-red)

本项目由BobAnkh发起，旨在为Linux初学者整理一些常用命令和常用工具的文档

项目网址：[https://blog.bobankh.com/LinuxBeginner/](https://blog.bobankh.com/LinuxBeginner/)

## To Do

- 为所有Linux命令进一步添加常用的使用情况样例以及注意事项
- 添加更多的常用工具

## How to Contribute

我们非常欢迎任何人为这个仓库添加新的内容，只要它对于这个仓库是具有意义的

### 关于提交的注意事项

#### 关于Pull Request

你需要在fork的仓库的一个具有与你所提交的内容相关名称的单独的branch提起Pull Request（PR），同时，从master分支提起的PR将不会被接受。这是因为你从单独分支提起PR时，仍可以通过向该分支进行commit和push来修改内容、持续更新。

对于本项目目前而言，提起的PR可以根据所属类别——Linux命令或Linux工具，分别以如下形式命名分支：`LinuxCommand/<number of command><command>`或`LinuxTool/<number of tool><tool>`

> 例如：LinuxCommand/01ls或LinuxTool/02htop等。

此外，在PR的信息框内简单描述本次PR的主要内容，以便reviewer可以较为容易的判断和了解你的想法，该部分不可空缺。同时，基于本项目的情况，可以在计划添加某一新命令或工具时，可以建立新的分支和相关文件后，以`draft pull request`的形式进行序号占位，需要选择已用序号后续紧邻的序号，并且不能够使用未被merge的PR所占用的序号。如果需要进行非内容方面的更改，建议先提出issue进行讨论。**如是对于内容的PR，则PR的标题应以`LinuxCommand:`或以`LinuxTool:`开头**

此外，若有对于html或css文件的修改，需要附上相应的截图

本仓库目前设置了一些自动化检查功能，在提交PR后可稍作等待，根据comment的内容来进行相应处理

#### 关于commit

每个commit建议包含相对单独的内容（即不建议将多类修改大杂烩在一个commit中提交），同时需要在message信息中体现出具体更改

本项目的commit信息规范主要参考目前使用最为广泛的[AngularJS Git Commit Message Conventions](https://docs.google.com/document/d/1QrDFcIiPjSLDn3EL15IJygNPiHORgU1_OOAqWjiDU5Y/edit#heading=h.uyo6cb12dt6w)：

> `<type>(<scope>): <subject>`
>
> // blank line
>
> `<body>`
>
> // blank line
>
> `<footer>`

对于任何项目而言，第一行即`<header>`部分是必须的，其后的`<body>`和`<footer>`则可依据实际情况予以省略

`<header>`部分仅有一行，其中必须填写`<type>`与`<subject>`字段，`<scope>`字段可以选填（但也建议填写）

`<type>`主要用于说明commit的类别，在`AngularJS Git Commit Message Conventions`中，只允许使用以下8个标识：

- feat: 增加新功能（feature）
- fix: 修补bug
- docs: 只改动了文档（documentation）相关的内容
- style: 格式，指不影响代码运行的变动或不影响代码含义的变动，例如去掉空格、改变缩进、增删分号等
- refactor: 重构（即不是新增功能，也不是修改bug的代码变动）
- test: 增加测试或修改现有测试
- chore: 构建过程或辅助工具的变动
- revert: 如果当前commit是用于撤销以前的commit，并在后面跟随被撤销commit的`<header>`，并且`<body>`部分需为执行`git revert`所打印的信息

对于本项目而言，如有需要，亦可使用如下标识：

- build: 构造工具或外部依赖的改动，如webpack, npm
- perf: 提高性能的改动
- ci: 与CI（持续集成）有关的改动

如一次改动中与多个`<type>`相关，则优先使用`feat`与`fix`，其次使用`AngularJS Git Commit Message Conventions`中规定的剩余6个，最后则是针对特殊需要的余下3个

`<scope>`中主要描述commit影响的范围，视具体改动情况而定，如可以填写所改动的文件（如有多个文件，则可以统一填写其所属模块或项目名）

`<subject>`中主要是本次commit目的的简短描述，要求以动词开头，使用第一人称现在时，并且首字母小写，结尾无需添加句号

`<body>`部分是对于本次commit的详细描述，建议使用`-`符号列写成多行，同样要求使用第一人称现在时，并且应当说明代码变动的动机以及与之前的差异对比

`<footer>`部分只适用于两种情况，若无此两种情况则可略去：其一是不兼容变动——即当前代码与上一版本不兼容，则需以`BREAKING CHANGE`开头描述变动本身、变动理由以及迁移方法；其二是与issue相关，如本次commit是针对某个issue做出的提交，可以在此部分以`Closes #123, #456`这样的形式关闭一个或多个issue

对于commit信息的`<header>`部分，应当尽量限制在50个字符内，对于其`<body>`部分，每一行应尽量限制在72个字符内

> 例如，对于ls.md的修改，commit信息可以写为：

```text
docs(ls.md): add linux command ls

- add basic usage format of command ls
- add arguments of command ls
- add considerations of command ls
- plan to add more common examples in future
- plan to add descriptions in the future
```

> 又例如，对于ls.md中发现书写错误的修改，commit信息可以写为：

```text
docs(ls.md): fix a typo

- change some `-` to `--`
```

### 关于内容的注意事项

> 目前主要以Linux命令和Linux工具为主要的工作重心，如果认为有其他方面也是可以添加的，欢迎提出issue或以类似的文件形式组织后pr

- 对于Linux命令而言，目前计划涉及内容如下：
    1. 命令格式
    2. 基本功能
    3. 常用参数
    4. 注意事项（这一项可以没有），例如：在rm命令中需要注意最好不要执行形如`sudo rm -rf /`这样的命令，以避免不必要的麻烦
    5. 常用形式，即常用命令参数及具体的使用场景，例如：ls命令常用`ls -al`以及`ls -hal`用于查看具体各文件情况，且后者是以human-readable形式呈现的

- 对于Linux工具而言，目前计划涉及内容如下：
    1. 基本功用介绍
    2. 如何安装
    3. 如何使用（可包含基本参数和基本指令）
    4. 常见使用方式和注意事项

**欢迎大家来为本项目贡献自己的力量，如果有问题欢迎随时提出issue或通过email等形式交流**
