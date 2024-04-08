#!/bin/bash

while true; do
    echo "1. Display the disk usage"
    echo "2. Display the memory usage"
    echo "3. Print the content of $1 file"
    echo "4. Exit"

    read -p "Choose your option [1-4]: " choice

    case $choice in
        1)
            echo ""
            echo "Disk Usage:"
            df -h
            ;;
        2)
            echo ""
            echo "Memory Usage:"
            free -h
            ;;
        3)
            echo ""
            echo "Content of $1 file:"
            while IFS= read -r line; do
                echo "$line"
            done < "$1"
            ;;
        4)
            echo "Bye!"
            exit 0
            ;;
        *)
            echo "Invalid option. Please choose between 1 and 4."
            ;;
    esac
done
