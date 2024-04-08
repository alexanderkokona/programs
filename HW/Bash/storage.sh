#!/bin/bash

while true; do
    echo "1. Display the disk usage"
    echo "2. Display the memory usage"
    echo "3. Print the content of $1 file"
    echo "4. Exit"

    read -p "Choose your option [1-4]: " choice

    if [ "$choice" == "1" ]; then
        echo ""
        echo "Disk Usage:"
        df -h
    elif [ "$choice" == "2" ]; then
        echo ""
        echo "Memory Usage:"
        free -h
    elif [ "$choice" == "3" ]; then
        echo ""
        echo "Content of $1 file:"
        while IFS= read -r line; do
            echo "$line"
        done < "$1"
    elif [ "$choice" == "4" ]; then
        echo "Bye!"
        exit 0
    else
        echo "Invalid option. Please choose between 1 and 4."
    fi
done
