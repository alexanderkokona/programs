#!/bin/bash

function make_file () {
    read -p "$2 does not exist. Do you want to create it? " ans
    if [[ $ans == "Y" || $ans == "y" ]] ; then
        echo creating $2 file in $1 directory
        touch $1/$2
        echo Here is the list of files in $1 directory
        ls -l $1
    else 
        echo Here is the list of files in $1 directory
        ls -l $1
        exit
    fi
}

if [[ -d $1 ]] ; then
    echo $1 directory exists.
    if [[ -f "$1/$2" ]] ; then
        echo $2 exists
    else
        make_file $1 $2
    fi
else
    read -p "$1 directory does not exist. Do you want to create it? " ans
    if [[ $ans == "Y" || $ans == "y" ]] ; then
        echo creating $1 directory
        mkdir $1
        make_file $1 $2 
    else 
        exit
    fi
fi
