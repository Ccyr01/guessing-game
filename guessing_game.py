"""
Christian Cyr
5/26/2025
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""

# Import the random and statistics modules.
import random
import statistics
import math
# Create the start_game function.
attempt_list = []


def start_game():
    attempts = 0

#   1. Display an intro/welcome message to the player.
    print("Welcome to the guessing game.")
#   2. Store a random number as the answer/solution.
    number_to_guess = random.randint(1,100)
#   3. Continuously prompt the player for a guess.
    while True:
        try:
            user_num = int(input("Guess a number between 1 and 100:\n>"))
            if user_num < 1 or user_num > 100:
                #TODO - Ask if attempts should still be counted
                print(f'{user_num} is out of range...\n Between 1 and 100 please')
            else:
        #     a. If the guess is greater than the solution, display to the player "It's lower".
                if user_num > number_to_guess:
                    print("It's lower.")
                    attempts += 1
        #     b. If the guess is less than the solution, display to the player "It's higher".
                elif user_num < number_to_guess:
                    print("It's higher.")
                    attempts += 1

        #   4. Once the guess is correct, stop looping, inform the user they "Got it" and store the number of guesses it took in a list.
                elif user_num == number_to_guess:
                    attempts += 1
                    print("Got it")
                    attempt_list.append(attempts)

                    break
                else:
                    print("please pick a valid number")                
        except ValueError:
            print("Invalid input! Please enter a number.")

    #   5. Display the following data to the player
    #     a. How many attempts it took them to get the correct number in this game
    print(f'# of Attempts: {attempts}')
    #     b. The mean of the saved attempts list
    print(f'Mean of the attempts: {statistics.mean(attempt_list)}')
    #     c. The median of the saved attempts list
    print(f'Median of the attempts: {statistics.median(attempt_list)}')
    #     d. The mode of the saved attempts list
    print(f'Mode of the attempts: {statistics.mode(attempt_list)}')

#   6. Prompt the player to play again

    play_again_choice = input("""Would you like to play again?\n
                          Select yes or y to play again
                          Select no or n to quit game\n>""")

    #     a. If they decide to play again, start the game loop over.
    if play_again_choice.lower() == 'y' or play_again_choice.lower() == "yes":
        print(f'High Score = {min(attempt_list)}')
        start_game()
    #     b. If they decide to quit, show them a goodbye message.
    elif play_again_choice.lower() == 'n' or play_again_choice.lower() == "no":
        print("Goodbye")
    # ( You can add more features/enhancements if you'd like to. )
    else:
        print("please enter yes or no")

# Kick off the program by calling the start_game function.
start_game()
