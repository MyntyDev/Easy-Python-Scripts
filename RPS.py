POSSIBILITIES = {

        "rock" : "paper",
        "paper" : "scissors",
        "scissors" : "rock"
}

def is_won(user_choice : str, computer_choice : str) -> bool:

    global POSSIBILITIES 

    return POSSIBILITIES[computer_choice] == user_choice 

def main():
    valid = ["rock", "paper", "scissors"]
    user_choice = input("What is your choice? (rock, paper, or scissors) --> ").lower()

    if user_choice not in valid:
        main()

    from random import choice 

    computer_choice = choice(valid)

    user_won = is_won(user_choice, computer_choice)

    if user_won:
        print("You won! Nice.")
    
    elif not user_won:
        print("You lost. That's not cool.")

    else:
        print("Tie!")

    main()

if __name__ == "__main__":
    main()