#!/bin/bash

function usage {
    cat <<"EOF"
Usage:
    writeup [init GENRE/EVENT_NAME|add CHALLENGE_NAME]

Commands:
    init GENRE/EVENT_NAME
        GENRE/EVENT_NAMEに対応するwriteup用のディレクトリを初期化します。
        GENREはcrypto|forensics|misc|pwn|reversing|web のいずれかの文字列です。
        EVENT_NAMEは、hoge_CTF_2023のようになります。例えば、

            $ writeup init crypto/hoge_CTF_2023

        のように使います。

    add CHALLENGE_NAME
        CHALLENGE_NAMEに対応するwriteupのテンプレートを作成します。
        ctf_practice/GENRE/EVENTディレクトリで実行してください。例えば、

            $ cd crypto/hoge_CTF_2023
            $ writeup add My_Question1

        のように使います。

EOF
}

function init {
    genre=$(dirname $1)
    event=$(basename $1)

    case "$genre" in
    crypto|forensics|misc|pwn|reversing|web)
        if ! [ -e "$1" ]; then
            mkdir $1
            echo -e "# $event\n## 問題" > $1/README.md
        else
            echo $1 is already exists.
        fi
        ;;
    *) 
        echo "Please chose the genre from [crypto|forensics|misc|pwn|reversing|web]."
        ;;
    esac
}

function add {
    check=$(basename $(cd ../../ && pwd))
    # イベントディレクトリ内かつ既に実行済みでないなら
    if [ "$check" == "ctf_practice" ] && ! [ -e $1 ]; then
        echo -e "* [$1](./$1.md)" >> ./README.md
        mkdir $1
        mkdir $1/given_files
        mkdir $1/solve
        touch $1/solve/writeup.md
        mkdir $1/assets
        echo -e "# $1\n\n(ここに問題文を書いてください)\n\n# Solution\n[Writeup](./solve/writeup.md)" >> $1/README.md
        echo -e "# My solution for $1\n" >> $1/solve/writeup.md
    fi
}

case "$1" in
init )
    init $2
    ;;
add )
    add $2
    ;;
*)
    usage
    ;;
    

esac
