import random
import sys

OPTIONS = ["rock", "paper", "scissors"]

def main():
    user_wins = 0
    computer_wins = 0
    game_count = 0

    while True:
        user_guess = input("Type Rock/Paper/Scissors or Q to quit: ").strip().lower()

        if user_guess == 'q':
            print_summary(user_wins, computer_wins, game_count)
            sys.exit("Good Bye!")
            
        if user_guess not in OPTIONS:
            print("Invalid input. Please type Rock, Paper, Scissors, or Q to quit.")
            continue
        
        game_count += 1
        
        random_number = random.randint(0, 2)
        computer_guess = OPTIONS[random_number]
        print(f"Computer guess: {computer_guess}")


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
    if game_count > 0:
        print(f"You won {user_wins} times.")
        print(f"Computer won {computer_wins} times.")

        if user_wins > computer_wins:
            print(f"\"You are the Winner.\"")
        elif user_wins < computer_wins:
            print(f"\"Computer is the Winner.\"")
        else:
            print(f"\"It is Tie Game\"")
        print("Thank you! For Playing.")
    else:
        print("No games played. Thank you for trying!")



if __name__ == "__main__":
    main()
   
    


        

        

        

