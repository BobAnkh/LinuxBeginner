#!/bin/bash
sudo apt-get install pandoc                                        #安装pandoc
wget -qO- "https://yihui.org/gh/tinytex/tools/install-unx.sh" | sh #安装TinyTex
export PATH=$PATH:$HOME/bin                                        #将Tex相关可执行文件添加到PATH
#安装其他一些必要的Tex包
tlmgr install unicode-math filehook xecjk xltxtra realscripts fancyhdr lastpage ctex ms cjk ulem environ trimspaces zhnumber collection-fontsrecommended
#遍历repo下的文件，将所有md文件转换到$GITHUB_WORKSPACE/PDFs路径下变成pdf文件
DOC_PATH=$GITHUB_WORKSPACE/docs
PDF_PATH=$GITHUB_WORKSPACE/pdfs
trave_conv() {
    for file in $(ls "$DOC_PATH"/"$1"); do
        if [ -f "$DOC_PATH"/"$1"/"$file" ]; then
            if [[ "$file" =~ .md ]]; then
                if [ ! -d "$PDF_PATH"/"$1" ]; then
                    mkdir -p "$PDF_PATH"/"$1"
                fi
                echo "-----NOW CONVERTING""$1"/"$file""-----"
                pandoc "$DOC_PATH"/"$1"/"$file" -o "$PDF_PATH"/"$1"/"${file//'.md'/'.pdf'}" --pdf-engine=xelatex -V mainfont='PingFang SC' --template="$GITHUB_WORKSPACE"/scripts/template.tex
            fi
        else
            trave_conv "$1"/"$file"
        fi
    done
}
rm -rf "$PDF_PATH"
mkdir -p "$PDF_PATH"
trave_conv LinuxCommand
trave_conv LinuxTool
