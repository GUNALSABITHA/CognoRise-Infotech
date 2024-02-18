import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (r for rock, p for paper, s for scissors): ").lower()
        if user_choice in ['r', 'p', 's']:
            return user_choice
        else:
            print("Invalid choice. Please choose r for rock, p for paper, or s for scissors.")

def get_computer_choice():
    return random.choice(['r', 'p', 's'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'r' and computer_choice == 's') or \
         (user_choice == 'p' and computer_choice == 'r') or \
         (user_choice == 's' and computer_choice == 'p'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_score = 0
    computer_score = 0
    
    while True:
        print("\nRock, Paper, Scissors")
        print("----------------------")
        
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        if user_choice == 'r':
            user_choice_name = 'rock'
        elif user_choice == 'p':
            user_choice_name = 'paper'
        else:
            user_choice_name = 'scissors'
        
        if computer_choice == 'r':
            computer_choice_name = 'rock'
        elif computer_choice == 'p':
            computer_choice_name = 'paper'
        else:
            computer_choice_name = 'scissors'
        
        print(f"\nYou chose: {user_choice_name}")
        print(f"Computer chose: {computer_choice_name}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        
        print(f"\nScore - You: {user_score}, Computer: {computer_score}")
        
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("\nThanks for playing!")
            break

play_game()
