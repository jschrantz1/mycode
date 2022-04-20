import random

while True:

    user_action = input("Enter a choice (rock, paper, scissors, lizard, spock):\n> ").lower()
    possible_actions = ["rock", "paper", "scissors", "lizard", "spock"]
    computer_action = random.choice(possible_actions)
    
    if user_action not in possible_actions:
        print(f"{user_action} is not a valid option.\n""Please choose from list provided.\n")
        continue
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    

    elif user_action == "rock":
        if computer_action == "scissors":
            print("and as it always has.. Rock crushes scissors! You win!")
        if computer_action == "lizard":
            print("Rock crushes lizard! You win!")
        if computer_action == "spock":
            print("Spock vaporizes rock! You lose! Live Long and Prosper.")
        if computer_action == "paper":
            print("Bazinga! Paper covers rock! You lose!")
        
            
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        if computer_action == "scissors":
            print("Bazinga! Scissors cuts paper! You lose!")
        if computer_action == "spock":
            print("Paper disproves Spock! You win!")
        if computer_action == "lizard":
            print("Bazinga! Lizard eats paper! You lose!")
        

    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        if computer_action == "rock":
            print("and as it always has.. Rock crushes scissors! You lose!")
        if computer_action == "lizard":
            print("Scissors decapitate lizard! You win!")
        if computer_action == "spock":
            print("Spock smashes scissors! You lose! Live long and prosper.")
        
   
    elif user_action == "spock":
         if computer_action == "paper":
             print("Paper disproves Spock! You lose! Live long and prosper.")
         if computer_action == "scissors":
             print("Spock smashes scissors! You win!")
         if computer_action == "rock":
             print("Spock vaporizes rock! You win!")
         if computer_action == "lizard":
             print("Lizard poisons Spock! You lose! Live long and prosper.")
         

    elif user_action == "lizard":
         if computer_action == "paper":
             print("Lizard eats paper! You win!")
         if computer_action == "rock":
             print("Bazinga! Rock crushes lizard! You lose!")
         if computer_action == "scissors":
             print("Bazinga! Scissors decapitate lizard! You lose!")
         if computer_action == "spock":
             print("Lizard poisons Spock! You win!")
         

    play_again = input("\nIt must be humbling to suck on so many levels!\n" "Play again? (y/n):\n>")
    if play_again.lower() != "y":
        break
