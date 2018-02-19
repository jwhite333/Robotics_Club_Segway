#!/bin/bash

function file_exists() {
    # Boolean file check
    if [ -f $1 ];
    then
        echo "$1 does exist"
        return 1
    else
        echo "$1 doesn't exist"
        return 0
    fi
}

function do_install() {
    if file_exists $USER/home/.bashrc;
    then
        echo "Its good!"
    else
        echo "Meep"
    fi
}
