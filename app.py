import random

def main():
    print('Welcome to the game!')
    name = input("Enter your name: \n")
    print(f"Hello {name}!")
    startGame()

def startGame():
    print("The game has begun.")
    game = True
    while game == True:
        choice = input("Enter 'rock', 'paper', or 'scissors'.\n")
        if choice != "rock" and  choice != "paper" and choice != "scissors":
            print("Try again.")
            continue
        else:
            computerChoice = random.randint(1, 3)
            if choice == 'rock':
                choice = 1
            elif choice == 'paper':
                choice = 2
            else:
                choice = 3
            if choice == computerChoice:
                print("Tie!")
                again = input("Play again?\n")
                if again == "yes":
                    continue
                elif again == "no":
                    game = False
                    continue
                else:
                    print("Incorrect input. Game will terminate.")
                    game = False
                    continue
            
            



main()