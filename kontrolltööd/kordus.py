"""KORDUS
Küsi kasutajalt kordamööda paaris ja paarituid arve.

Kontrolli ja kuva ekraanile, et sisestatakse õige arv.

Lõpeta programm, kui kasutaja on 5 korda eksinud.
"""
def game_mode_choice():
    choice = None
    choices = ["1", "2"]
    print("")
    while True:
        print("1. Guessing game.")
        print("2. Number input.")
        choice = input("Please insert 1 or 2 for the corresponding mode(1/2): ")
        if choice == choices[0]:
            print("Good luck guessing!")
            print("")
            return True
        elif choice == choices[1]:
            print("A simple task awaits you!")
            print("")
            return False
        else:
            print("You have to insert between 1 or 2 and without spaces :)")


def even_or_uneven_guess_randomizer():
    import random
    if random.randint(1,2) == 1:
        return "even"
    else:
        return "uneven"


def even_number_check(number):
    if number in user_guesses_array:
        return "Repeat"
    elif number == 0:
        return "Zero"
    elif number % 2 == 0:
        user_guesses_array.append(number)
        return "even"
    else:
        user_guesses_array.append(number)
        return "uneven"

def user_input_str_to_int():
    user_str = input("Please enter a whole number: ")
    while True:
        try:
            user_int = int(user_str)
            return user_int
        except ValueError:
            user_str = input("Please enter a valid whole number: ")

def user_guess_check(user_guess,wanted_guess, fails, points):
    if user_guess == wanted_guess:
        print(f"And an {wanted_guess} number was the correct guess!")
        points = points + 1
        return points, fails
    elif user_guess == "Repeat":
        print("You can't choose the same number twice.")
        fails = fails + 1
        print(f"You have {5 - fails} tries left.")
        return points, fails
    elif user_guess == "Zero":
        print("Zero can't be either silly!")
        fails = fails + 1
        print(f"You have {5 - fails} tries left.")
        return points, fails
    else:
        print("Ouch! That wasn't right.")
        fails = fails + 1
        print(f"You have {5 - fails} tries left.")
        return points, fails


def guessing_game():
    points = 0
    fails = 0
    while True:
        print("")
        print("Even or uneven?")
        wanted_guess = even_or_uneven_guess_randomizer()
        user_guess = even_number_check(user_input_str_to_int())
        points, fails = user_guess_check(user_guess, wanted_guess, fails, points)

        if fails == 5:
            print(f"You lost the game! Your total points were {points}")
            print("Better luck next time!")
            break

def number_input():
    fails = 0
    while True:
        wanted_number = even_or_uneven_guess_randomizer()
        print(f"You need to enter an {wanted_number} number.")
        user_input = even_number_check(user_input_str_to_int())

        if user_input == "Repeat":
            print("You cannot enter the same number twice!")
            fails += 1
            print("")
        elif user_input == wanted_number:
            print("")
        else:
            print(f"Unfortunately the number was not {wanted_number}")
            fails += 1
            print("")

        if fails == 5:
            print(f"You inserted the wrong number too many times.")
            print("Better luck next time!")
            break

def application_exit():
    correct_answers_array = ["y","yes","positive","n","no","negative"]
    while True:
        user_input = input("Do you want to continue?(Y/N): ").lower()
        if user_input in correct_answers_array[0:2]:
            user_guesses_array = []
            return True, user_guesses_array
        elif user_input in correct_answers_array[3:5]:
            return False
        else:
            print("Please enter a valid input.")

print("Welcome to the even number guessing game!")
print("You have to insert a whole number to check if your guess was correct.")
print("If it is, you get a point, if it isn't you get 5 tries before you lose the game.")
print("Or, if you choose to, you can just insert even or uneven numbers in turn without repeating them and you have 5 tries to insert a correct number.")
print("You can not choose the same number more than once.")

user_guesses_array = []

while True:
    game_mode = game_mode_choice()
    if game_mode == 1:
        #Guessing game
        guessing_game()
    else:
        #Number input
        number_input()

    #Application exit
    if not application_exit():
        break