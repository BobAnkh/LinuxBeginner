# CONTRIBUTING

非常高兴您愿意为本项目贡献自己的力量，欢迎随时提出issue或者提交pull request，请注意按照各自的template进行撰写，我们采用了一系列自动化工具来检查，不符合规范的贡献可能会被拒绝，相关规范如下

## 关于Commit的规范

每个commit应当包含相对独立的内容（即不允许将多类修改大杂烩在一个commit中提交），同时需要在message信息中体现出具体更改

本项目的commit信息规范主要参考目前使用最为广泛的[AngularJS Git Commit Message Conventions](https://docs.google.com/document/d/1QrDFcIiPjSLDn3EL15IJygNPiHORgU1_OOAqWjiDU5Y/edit#heading=h.uyo6cb12dt6w)，格式如下：

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

同时，需要注意，对于commit信息的`<header>`部分，应当尽量限制在50个字符及以内，对于其`<body>`部分，每一行应尽量限制在72个字符及以内

### 关于`<header>`部分

`<header>`部分仅有一行，三个字段`<type>`，`<scope>`和`<subject>`的要求如下：

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

`<scope>`中主要描述commit影响的范围，通常是文件、路径、功能，视具体改动情况而定，如可以填写所改动的文件（如有多个文件，则可以统一填写其所属模块或项目名），或者填写所影响的功能，若是全局性质的影响，可以填写`*`

`<subject>`中主要是本次commit目的的简短描述，要求以动词开头，使用第一人称现在时，并且首字母小写，结尾不应添加句号

### 关于`<body>`部分

`<body>`部分就是正文部分，是对于本次commit的详细描述，同样要求使用第一人称现在时

该部分在`<header>`足以概括本commit内容时可以略去

建议使用`-`符号列写成多行，并且应当说明说明本次提交解决了什么问题，如何解决的以及是否引入了其他修改（如必要的文档更新等）

### 关于`<footer>`部分

`<footer>`部分只适用于两种情况，若无此两种情况则可略去：

其一是不兼容变动，即当前代码与上一版本不兼容，则需以`BREAKING CHANGE`开头描述变动本身、变动理由以及迁移方法

其二是与issue相关，如本次commit是针对某个issue做出的提交，可以在此部分以`Closes #123, #456`这样的形式关闭一个或多个issue

### Commit信息示例

以下给出一些commit信息的示例：

> 例如，创建了新的文件ls.md以增加新的Linux命令ls，commit信息可以写为：

```text
feat(command): add a new linux command ls

- add basic usage format of command ls
- add arguments of command ls
- add considerations of command ls
- plan to add more typical examples in future
- plan to add descriptions in the future
```

> 又例如，对于ls.md中发现书写错误的修改，commit信息可以写为：

```text
docs(ls): fix a typo

- change `-` to `--`

Closes #4
```

## 关于Pull Request的规范

### 关于Pull Request的分支规范

你需要在fork的仓库的一个具有与你所提交的内容相关名称的单独的branch提起Pull Request（PR）。从master分支提起的Pull Request将不会被接受。这是因为你从单独分支提起Pull Request时，仍可以通过向该分支进行commit和push来修改内容、持续更新

对于本项目目前而言，Pull Request主要可以使用的分支命名规范如下：

- 如果是开发新功能，分支名称需以`feature/`开头，后接具体的功能名称，如`feature/md2pdf`，若是基于某现有功能的优化，则可为`feature/optimize_md2pdf`
- 如果是对于功能的bug的修复，则分支名称需以`fix/`开头，后接具体修复的功能名称，如`fix/yapf`
- 如果是对于文档内容的修改，对于本项目而言，则可以根据所属类别——Linux命令或Linux工具，分别以如下形式命名分支：`LinuxCommand/<number of command><command>`或`LinuxTool/<number of tool><tool>`，如：`LinuxCommand/01ls`或`LinuxTool/02htop`
- 如果是其他情况，请务必先提出issue与维护者进行讨论

### 关于Pull Request的描述信息规范

请按照[pull_request_template](.github/PULL_REQUEST_TEMPLATE.md)描述本次Pull Request的相关内容，以便reviewer可以较为容易地判断和了解你的想法，该部分不可空缺。

**如是对于文档内容变更的PR，则PR的标题应以`docs(LinuxCommand):`或以`docs(LinuxTool):`开头；开发新功能的PR，标题应以`feature(<Your-New-Feautre>):`开头；修复bug的PR，标题应以`fix(<Your-BugFix-Feature>):`开头**

在Pull Request的信息框内，需要描述本变更的意义（如解决了什么问题、优化完善了什么内容等），详细描述这个Pull Request中所实现的主要内容或功能，并介绍实现所采用的技术栈（如果有），以及产生的其他必要变更（如必要的文档更新）。

建议配合使用`Tasklist`形式，以更加直观地组织PR描述。请注意，**任何`draft pull request`必须要在描述中包含`Tasklist`**，并随着你的提交和进展更新进度。如果本Pull Request解决了某一个issue，也请在描述中以正确的形式进行链接。此外，也需要检查未与已有的issue或Pull Request重复。并且，若有对于html或css文件的修改，需要在Pull Request描述中附上相应的截图

> Tasklist形式如下:
>
> [x] This is what you have done and how you achieve this.
>
> [ ] This is what you plan to do and how you plan to achieve it.

同时，基于本项目的情况，建议在计划添加某一新命令或工具时，或者开发新的功能时，建立新的分支和相关文件后，以`draft pull request`的形式进行占位。对于新的命令或工具，需要以此选择序号，并应当使用已用序号后续紧邻的序号，并且不能够使用未被merge的Pull Request所占用的序号。如果需要进行功能方面的更改，建议先提出**issue**或发起**draft pull request**进行讨论。

本仓库目前设置了一些自动化检查功能，在提交Pull Request后可稍作等待，可以根据comment的内容和check的details来进行相应处理

## 关于文档内容变更的注意事项

> 目前主要以Linux命令和Linux工具为主要的文档工作重心，如果认为有其他方面也是可以添加的，欢迎提出issue或以类似的文件形式组织后发起Pull Request

- 对于Linux命令而言，目前计划涉及内容如下：
    1. 命令格式
    2. 基本功能
    3. 常用参数
    4. 注意事项（这一项可以没有），例如：在rm命令中需要注意最好不要执行形如`sudo rm -rf /`这样的命令，以避免不必要的麻烦
    5. 典型示例，即常用命令参数及具体的使用场景，例如：ls命令常用`ls -al`以及`ls -hal`用于查看具体各文件情况，且后者是以human-readable形式呈现的

- 对于Linux工具而言，目前计划涉及内容如下：
    1. 基本功用介绍
    2. 如何安装
    3. 如何使用（可包含基本参数和基本指令）
    4. 常见使用方式和注意事项

## 关于各类型文件的要求

对于各类型文件，均应根据要求先在本地进行相应测试检查，并在通过后提交

### Markdown

采用markdownlint进行检查，具体配置可参考[.markdownlint.json](/.markdownlint.json)

### Python

采用flake8默认配置进行检查，并采用yapf默认配置进行格式化

### Shell

采用shellcheck默认配置进行检查
