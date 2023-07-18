#!/bin/bash

function usage {
    cat <<"EOF"
Usage:
    writeup [init GENRE/EVENT_NAME|add CHALLENGE_NAME]

Commands:
    init GENRE/EVENT_NAME

        Initialize the writeup directory that corresponds to `GENRE/EVENT_NAME`.
        GENRE is [crypto|forensics|misc|pwn|reversing|web] and EVENT_NAME is 
        like `hoge_CTF_2023`. For example: 

            $ writeup init crypto/hoge_CTF_2023

    add CHALLENGE_NAME
        Generate the writeup template that corresponds to CHALLENGE_NAME.
        This command has to be run in `ctf_practice/GENRE/EVENT` directory.
        For example: 

            $ cd crypto/hoge_CTF_2023
            $ writeup add My_Question1

EOF
}

function init {
    genre=$(dirname $1)
    event=$(basename $1)

    case "$genre" in
    crypto|forensics|misc|osint|pwn|reversing|web)
        if ! [ -e "$1" ]; then
            mkdir $1
            echo -e "# $event\n## 問題" > $1/README.md
        else
            echo $1 is already exists.
        fi
        ;;
    *) 
        echo "writeup init: Please chose the genre from [crypto|forensics|misc|osint|pwn|reversing|web]."
        ;;
    esac
}

function add {
    chal=$1

    # `add` should be run under the `ctf_practice/GENRE/EVENT` directory,
    # and is determined by whether or not the two upper directory name is `ctf_practice`.
    if ! [ "$(basename $(cd ../../ && pwd))" == "ctf_practice" ]; then
        echo "writeup add: Please run under the \`ctf_practice/ジャンル/イベント名/\` directory "
    elif [ -e $chal ]; then
        echo "writeup add: \`$chal\` already exists"
    else
        # generate template
        echo -e "* [$chal](./$chal/README.md)" >> ./README.md
        mkdir $chal
        mkdir $chal/given_files
        mkdir $chal/solve
        touch $chal/solve/writeup.md
        mkdir $chal/assets
        echo -e "# $chal\n\n(ここに問題文を書いてください)\n\n# Solution\n[Writeup](./solve/writeup.md)" >> $chal/README.md
        echo -e "# My solution for $chal\n" >> $chal/solve/writeup.md
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
