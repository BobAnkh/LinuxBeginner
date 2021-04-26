#!/bin/bash
shopt -s expand_aliases
sudo apt-get install pandoc #安装pandoc

#安装TinyTex
#设置安装路径，如果TMPDIR为空值，则等价于cd /tmp
cd "${TMPDIR:-/tmp}" || exit

#根据操作系统来设置安装路径和安装命令
if [ "$(uname)" = 'Darwin' ]; then
    TEXDIR=${TINYTEX_DIR:-~/Library/TinyTeX}
else
    TEXDIR=${TINYTEX_DIR:-~/.TinyTeX}
fi

#在当前目录下载install-tl-unx.tar.gz和tinytex.profile两个文件
rm -f install-tl-unx.tar.gz tinytex.profile
echo "Downloading install-tl-unx.tar.gz to ${PWD} ..."
TLREPO="${CTAN_REPO:-http://mirrors.ibiblio.org/CTAN/systems/texlive/tlnet}"
TLURL="${TLREPO}/install-tl-unx.tar.gz"
cp "$GITHUB_WORKSPACE"/scripts/tinytex.profile ./
if [ "$(uname)" = 'Darwin' ]; then
    curl -LO "$TLURL"
else
    wget "$TLURL"
    # ask `tlmgr path add` to add binaries to ~/bin instead of the default
    # /usr/local/bin unless this script is invoked with the argument '--admin'
    # (e.g., users want to make LaTeX binaries available system-wide), in which
    # case we personalize texmf variables
    if [ "$1" = '--admin' ]; then
        {
        echo "TEXMFCONFIG $HOME/.TinyTeX/texmf-config
        TEXMFHOME $HOME/.TinyTeX/texmf-home
        TEXMFVAR $HOME/.TinyTeX/texmf-var"
        } >>tinytex.profile
    else
        mkdir -p "$HOME/bin"
        echo "tlpdbopt_sys_bin ${HOME}/bin" >>tinytex.profile
    fi
fi

# no need to personalize texmf variables if not installed by admin
if [ "$1" != '--admin' ]; then
    {
    echo "TEXMFCONFIG $TEXMFSYSCONFIG
    TEXMFHOME $TEXMFLOCAL
    TEXMFVAR $TEXMFSYSVAR"
    } >>tinytex.profile
fi

tar -xzf install-tl-unx.tar.gz
rm install-tl-unx.tar.gz

mkdir texlive
cd texlive || exit
TEXLIVE_INSTALL_ENV_NOCHECK=true TEXLIVE_INSTALL_NO_WELCOME=true "../install-tl-*/install-tl" -no-gui -profile=../tinytex.profile -repository "$TLREPO"
rm -r ../install-tl-* ../tinytex.profile install-tl.log

alias tlmgr='./bin/*/tlmgr'

tlmgr option repository "$TLREPO"

if [ "$3" != '' ]; then
    tlmgr option repository "$3"
    if [ "$4" != '' ]; then
        tlmgr --repository http://www.preining.info/tlgpg/ install tlgpg
    fi
    # test if the repository is accessible; if not, set the default CTAN repo
    tlmgr update --list || ./tlmgr option repository ctan
fi
tlmgr install latex-bin luatex xetex

cd ../ || exit
rm -rf "$TEXDIR"
mkdir -p "$TEXDIR"
mv texlive/* "$TEXDIR"
rm -r texlive

echo "---------install pkgs!!!!!!----------"
#$TEXDIR/bin/*/tlmgr install $(download https://yihui.org/gh/tinytex/tools/pkgs-custom.txt | tr '\n' ' ')
#download https://yihui.org/gh/tinytex/tools/pkgs-custom.txt | tr '\n' ' ' | $TEXDIR/bin/*/tlmgr install
#$TEXDIR/bin/*/tlmgr install $(cat $GITHUB_WORKSPACE/scripts/pkgs-custom.txt | tr '\n' ' ')
#cat $GITHUB_WORKSPACE/scripts/pkgs-custom.txt | tr '\n' ' ' | $TEXDIR/bin/*/tlmgr install
"$TEXDIR/bin/*/tlmgr" install amsfonts amsmath atbegshi atveryend auxhook bibtex bigintcalc bitset booktabs dvips ec epstopdf-pkg etexcmds etoolbox euenc fancyvrb filehook float fontspec framed geometry gettitlestring grffile helvetic hycolor hyperref iftex inconsolata infwarerr intcalc kvdefinekeys kvoptions kvsetkeys latex-amsmath-dev latex-tools-dev latexmk letltxmacro lm-math ltxcmds lualatex-math mdwtools metafont mfware natbib pdfescape pdftexcmds refcount rerunfilecheck stringenc tex times tipa tools unicode-math uniquecounter url xcolor xkeyval xunicode zapfding unicode-math filehook xecjk xltxtra realscripts fancyhdr lastpage ctex ms cjk ulem environ trimspaces zhnumber collection-fontsrecommended

#根据操作系统来添加path，虽然现在貌似是不work的状态
if [ "$1" = '--admin' ]; then
    if [ "$2" != '--no-path' ]; then
        sudo "$TEXDIR/bin/*/tlmgr" path add
    fi
else
    "$TEXDIR/bin/*/tlmgr" path add || true
fi

export PATH=$PATH:$HOME/bin #将Tex相关可执行文件添加到PATH

#遍历repo下的文件，将所有md文件转换到$GITHUB_WORKSPACE/PDFs路径下变成pdf文件
DOC_PATH=$GITHUB_WORKSPACE/docs
PDF_PATH=$GITHUB_WORKSPACE/pdfs
trave_conv() {
    for file in $(ls "$DOC_PATH"/"$1"); do
        if [ -f "$DOC_PATH"/"$1"/"$file" ]; then
            if [[ "$file" =~ cd.md$ ]]; then
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
