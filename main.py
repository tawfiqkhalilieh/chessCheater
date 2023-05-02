import os

print("\nPlease choose from the following options:\n\n")
print("1. Chess Cheater")
print("2. Chess Helper")
print("3. Puzzle Solver")
print("4. Times backend")
print("5. Learner backend")

print("\n\n0. exit")
val: str = input("\n")

clear_console= lambda: os.system('cls' if os.name=='nt' else 'clear')

if val == "1":
    clear_console()
    print("Please choose from the following options:")
    print("1. Play Online")
    print("2. Play 960chess")
    print("3. Play In The Analytics")
    print("4. Play Against Bots")

    choice: str = input()

    if choice == "1":
        print("Setup the VPN and then click on 'Start' button")
        print("Happy Hacking 🚀")
        from automation import main
    
    elif choice == "2":
        print("Setup the VPN and then click on 'Start' button")
        print("Happy Hacking 🚀")
        from chess960 import chess960

    elif choice == "3":
        print("Have fun 🎉")
        from automation.other import analytics
    elif choice == "4":
        print("Happy Playing 🚀")
        print("Choose the bot and wait 2 seconds")
        from automation.other import bot

    elif choice == '5':
        print("Happy Playing 🚀")
        print("Choose the bot and click enter")
        from chess960.other import bot

    else:
        print("Invalid Choice")

elif val == "2":
    clear_console()
    print("Happy Playing 🚀")
    from chessHelper import main

elif val == "3":
    clear_console()
    print("Login and click 'Enter' in the terminal")
    print("Happy Playing 🚀")
    from puzzle_solver import main

elif val == "4":
    clear_console()
    print('This service is under development ⚒️')

elif val == "5":
    clear_console()
    print('This service is under development ⚒️')