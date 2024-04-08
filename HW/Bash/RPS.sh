#!/bin/bash

# Rock Paper Scissors, you against the computer.

#script global variables to hold choices
computer_choice=-1
user_choice=-1

# generates the computer response
compute_computer_choice () {
    computer_choice=$(( ( RANDOM % 3 ) + 1 ))
    if [ $computer_choice -eq 1 ]; then
        echo "Computer chose: Rock"
    elif [ $computer_choice -eq 2 ]; then
        echo "Computer chose: Paper"
    else
        echo "Computer chose: Scissors"
    fi
}

# prints the users selection
print_user_choice () {
    if [ $user_choice -eq 1 ]; then
        echo "You chose: Rock"
    elif [ $user_choice -eq 2 ]; then
        echo "You chose: Paper"
    else
        echo "You chose: Scissors"
    fi
}

# decide who won the round.
compute_winner () {
    # Easiest to check if it is a tie first.  Then check every other possible combination of choices
    if [ $user_choice -eq $computer_choice ]; then
        echo "It's a tie! Try again."
    elif [ $user_choice -eq 1 ] && [ $computer_choice -eq 3 ]; then
        echo "You win!"
    elif [ $user_choice -eq 2 ] && [ $computer_choice -eq 1 ]; then
        echo "You win!"
    elif [ $user_choice -eq 3 ] && [ $computer_choice -eq 2 ]; then
        echo "You win!"
    else
        echo "Computer wins!"
    fi
}

# looping in while loop until 4 is pressed and then if breaks out of loop.
while true; do

    # Prompt player for choices and read in player selection.
    echo "Rock Paper Scissors Game"
    echo "1. Rock"
    echo "2. Paper"
    echo "3. Scissors"
    echo "4. Quit"
    read -p "Enter your choice: " user_choice

    # Check for "Quit" selection and handle that input
    if [ $user_choice -eq 4 ]; then
        break
    fi

    compute_computer_choice
    print_user_choice
    compute_winner
done

echo "Thanks for playing, goodbye."
