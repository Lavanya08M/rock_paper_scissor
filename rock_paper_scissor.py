import random
import sys

# Define the valid game options as a constant
OPTIONS = ["rock", "paper", "scissors"]

def main():
    """
    Main function to execute the Rock-Paper-Scissors game loop.
    Tracks user and computer wins and handles user inputs.
    """
    user_wins = 0
    computer_wins = 0
    game_count = 0

    # Game loop
    while True:
        # Prompt user for their choice
        user_guess = input("Type Rock/Paper/Scissors or Q to quit: ").strip().lower()

        # Exit the game if the user types 'q'
        if user_guess == 'q':
            print_summary(user_wins, computer_wins, game_count)
            sys.exit("Good Bye!") # Terminate the program
        
        # Validate user input
        if user_guess not in OPTIONS:
            print("Invalid input. Please type Rock, Paper, Scissors, or Q to quit.")
            continue
        
        # Increment game count for a valid round
        game_count += 1
        
        # Generate a random choice for the computer
        random_number = random.randint(0, 2)
        computer_guess = OPTIONS[random_number]
        print(f"Computer guess: {computer_guess}")

        # Determine the outcome of the round
        if user_guess == "rock" and computer_guess == "scissors":
            print("You won!")
            user_wins += 1
        elif user_guess == "paper" and computer_guess == "rock":
            print("You won!")
            user_wins += 1
        elif user_guess == "scissors" and computer_guess == "paper":
            print("You won!")
            user_wins += 1
        elif user_guess == computer_guess:
            print("It's a tie.")
        else:
            print("You lost!")
            computer_wins += 1

def print_summary(user_wins, computer_wins, game_count):
    """
    Prints a summary of the game results after the user quits.
    :param user_wins: Total number of rounds won by the user
    :param computer_wins: Total number of rounds won by the computer
    :param game_count: Total number of games played
    """
    if game_count > 0:
        # Print detailed game results
        print(f"You won {user_wins} times.")
        print(f"Computer won {computer_wins} times.")

        # Determine the overall winner
        if user_wins > computer_wins:
            print(f"\"You are the Winner.\"")
        elif user_wins < computer_wins:
            print(f"\"Computer is the Winner.\"")
        else:
            print(f"\"It is Tie Game\"")
        print("Thank you! For Playing.")
    else:
        # Handle case where no games were played
        print("No games played. Thank you for trying!")

# Entry point of the program
if __name__ == "__main__":
    main()
   
    


        

        

        

