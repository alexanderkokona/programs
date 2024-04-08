#!/bin/bash

# Rock Paper Scissors, you against the computer.

#script global variables to hold choices
computer_choice=-1
user_choice=-1

# generates the computer response
compute_computer_choice () {
	computer_choice=$(( ( RANDOM % 3 ) + 1 ))
	#  TODO: Write the logic to print the computer's choice after it is generated.
	#  This will be a series of if and else if statements checking for each possible computer choice.

}

# prints the users selection
print_user_choice () {
	#  TODO: Write the logic to print the player's  response after it is selected by the player.
	#  This will be a series of if and else if statements checking for each possible user choice, like the computer choice.
}

# decide who won the round.
compute_winner () {
	# Easiest to check if it is a tie first.  Then check every other possible combination of choices
	if (( user_choice == computer_choice )); then
               echo "You tied.  Try again"
        elif (( user_choice == 1 && computer_choice == 3  )); then
               echo "You win!"

	# TODO: Finish the series of elif statements to check the remaining choices of player and computer.  


        fi
}

# looping in while loop until 4 is pressed and then if breaks out of loop.

# TODO: write loop logic which then will end with the done statement below.

	# TODO: Prompt player for choices and read in player selection.
	# Check for "Done" selection and handle that input
	
	
	# TODO: call each of the three functions you have finished above in the first order.
	
done

echo "Thanks for playing, goodbye."
